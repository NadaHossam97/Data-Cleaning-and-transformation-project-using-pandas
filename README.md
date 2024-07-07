# Data Cleaning and Transformation Project using Pandas
**Overview**

This project involves preprocessing and transforming a dataset obtained from the Bank for International Settlements (BIS) for further analysis. The dataset contains financial and economic data reported by various institutions and countries over time.

## Goals

1.  **Data Cleaning**: Remove unnecessary columns and rename columns for clarity.
2.  **Standardization**: Standardize values in certain columns for consistency and readability.
3.  **Data Parsing**: Extract relevant information from specific columns for deeper analysis.
4.  **Date Handling**: Convert date columns to datetime format and extract additional temporal features.

## Steps Taken

### Step 1: Data Reading

-   **Code**: Reads the dataset stored in a CSV file (`bisdata.csv`) into a pandas DataFrame for initial processing.

### Step 2: Column Cleanup

-   **Code**: Drops columns that are deemed unnecessary for the analysis, such as identifiers and metadata fields.

### Step 3: Column Renaming

-   **Code**: Renames columns to more meaningful names using a dictionary mapping.

### Step 4: Value Standardization

-   **Code**: Standardizes specific values within selected columns to simplify analysis and interpretation.

### Step 5: Data Parsing and Transformation

-   **Code**: Splits and extracts information from certain columns (`Parent country` and `Position type`) to enhance dataset clarity.

### Step 6: Date Handling

-   **Code**: Converts the `Period` column to datetime format and extracts year, month, and day components for temporal analysis.

## Outputs

-   **Modified Dataset**: The processed DataFrame (`bis`) with cleaned, standardized, and transformed data ready for further analysis or visualization.
-   **Documentation**: This markdown document serves as documentation detailing the steps taken in preprocessing and transforming the dataset.

## Conclusion

This project demonstrates the initial steps in data preparation for financial and economic analysis using Python and pandas. The resulting dataset (`bis`) is now structured and formatted for easier exploration and deeper insights into the BIS data.**
