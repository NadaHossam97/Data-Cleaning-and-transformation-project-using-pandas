import pandas as pd

bis = pd.read_csv("./bisdata.csv")

#Drop unnecessary columns 
bis = bis.drop(columns=['DATAFLOW_ID:Dataflow ID', 'KEY:Timeseries Key','FREQ:Frequency','L_INSTR:Type of instruments','L_DENOM:Currency denomination','L_REP_BANK_TYPE:Type of reporting institutions','L_REP_CTY:Reporting country','L_CP_COUNTRY:Counterparty country','Unit','Unit multiplier','OBS_CONF:Confidentiality','OBS_PRE_BREAK:Pre-break value','OBS_STATUS:Status'])

#Rename data columns 
column_mapper = {'L_MEASURE:Measure':'Measure','L_POSITION:Balance sheet position':'Balance sheet position','L_CURR_TYPE:Currency type of reporting country':'Currency type of reporting country','L_PARENT_CTY:Parent country':'Parent country','L_CP_SECTOR:Counterparty sector':'Counterparty sector','L_POS_TYPE:Position type':'Position type','TIME_PERIOD:Period':'Period','OBS_VALUE:Value':'Value'}
bis.rename(columns=column_mapper, inplace=True)

#Rename frequent values to a more convenient name
replace_values = {
    'F:FX and break adjusted change (BIS calculated)': 'FX',
    'G:Annual growth (BIS calculated)': 'Annual growth',
    'S:Amounts outstanding / Stocks': 'outstanding/Stocks',
    'C:Total claims': 'claims',
    'L:Total liabilities': 'liabilities',
    'A:All currencies (=D+F+U)': 'All Curr',
    'D:Domestic currency (ie currency of bank location country)': 'LCY',
    'F:Foreign currency (ie currencies foreign to bank location country)': 'FCY'
}
bis = bis.replace(replace_values)
bis[['Country Code','Parent country']]=bis['Parent country'].str.split(pat=':',expand=True)
bis[['part1','Position type']]=bis['Position type'].str.split(pat=':',expand=True)
bis[['part2','Counterparty sector']]=bis['Counterparty sector'].str.split(pat=':',expand=True)

bis = bis.drop(columns=['part1','part2'])

#Change datatype to datetime
bis['Period']=pd.to_datetime(bis['Period'])
bis['year']=bis['Period'].dt.year
bis['month']=bis['Period'].dt.month
bis['day']=bis['Period'].dt.day

bis.info()
print(bis['Counterparty sector'])
