import pandas as pd

bis = pd.read_csv("./bisdata.csv")

#Drop unnecessary columns 
bis = bis.drop(columns=['DATAFLOW_ID:Dataflow ID', 'KEY:Timeseries Key','FREQ:Frequency','L_INSTR:Type of instruments','L_DENOM:Currency denomination','L_REP_BANK_TYPE:Type of reporting institutions','L_REP_CTY:Reporting country','L_CP_COUNTRY:Counterparty country','Unit','Unit multiplier','OBS_CONF:Confidentiality','OBS_PRE_BREAK:Pre-break value','OBS_STATUS:Status'])

#Rename data columns 
column_mapper = {'L_MEASURE:Measure':'Measure','L_POSITION:Balance sheet position':'Balance sheet position','L_CURR_TYPE:Currency type of reporting country':'Currency type of reporting country','L_PARENT_CTY:Parent country':'Parent country','L_CP_SECTOR:Counterparty sector':'Counterparty sector','L_POS_TYPE:Position type':'Position type','TIME_PERIOD:Period':'Period','OBS_VALUE:Value':'Value'}
bis.rename(columns=column_mapper, inplace=True)

#Rename frequent values to a more convenient name
bis=bis.replace(['F:FX and break adjusted change (BIS calculated)','G:Annual growth (BIS calculated)','S:Amounts outstanding / Stocks'],['FX','Annual growth','outstanding/Stocks'])
bis=bis.replace(['C:Total claims','L:Total liabilities'],['claims','liabilities'])
bis=bis.replace(['A:All currencies (=D+F+U)','D:Domestic currency (ie currency of bank location country)','F:Foreign currency (ie currencies foreign to bank location country)'],['All Curr','LCY','FCY'])
bis[['code','Parent country']]=bis['Parent country'].str.split(pat=':',expand=True)
bis[['part1','Position type']]=bis['Position type'].str.split(pat=':',expand=True)
bis = bis.drop(columns=['code','part1'])

#Change datatype to datetime
bis['Period']=pd.to_datetime(bis['Period'])
bis['year']=bis['Period'].dt.year
bis['month']=bis['Period'].dt.month
bis['day']=bis['Period'].dt.day
