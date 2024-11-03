# Lending Club Loan Analysis - ELVTR Data Science Course Project

This project is part of the ELVTR Data Science course, designed to demonstrate the application of data science skills in a financial context. The primary goal is to analyse and model a dataset of loan applications to predict loan approval statuses.

## Project Objectives

1. **Data Cleaning and Preprocessing**: 
   - Handle missing values and inconsistent data types.
   - Remove duplicate entries, standardise, and normalise features.
2. **Feature Engineering and Selection**:
   - Categorise features into logical groups for better interpretability (e.g., credit history, employment information, loan performance).
   - Filter relevant features for modelling.
3. **Exploratory Data Analysis (EDA)**:
   - Perform statistical analysis and visualisation to uncover trends and insights.
4. **Predictive Modelling**:
   - Train and evaluate a predictive model for loan status classification.
   - Implement binary and multi-class classification using techniques like one-vs-one and one-vs-rest strategies.

## Project Workflow

1. **Data Loading**:
   - Load the main loan dataset and data dictionary to understand feature meanings and relationships.
2. **Data Cleaning**:
   - Ensure all columns are properly named and cleaned.
   - Address issues with missing and inconsistent data.
3. **Feature Engineering**:
   - Group features into categories like `Credit History`, `Employment Information`, and `Loan Performance`.
   - Create lists of pre- and post-hardship features to structure further analysis.
4. **Exploratory Data Analysis (EDA)**:
   - Visualise data distributions and correlations between features.
   - Identify key insights about loan performance and borrower profiles.
5. **Modelling**:
   - Prepare data for modelling with selected features.
   - Implement and evaluate models based on chosen evaluation metrics.

## Key Concepts Demonstrated

- **Data Cleaning**: Importance of preprocessing to ensure data quality.
- **Feature Selection**: Methods to retain meaningful variables for modelling.
- **Exploratory Analysis**: Using visualisations to understand trends.
- **Predictive Modelling**: Application of machine learning algorithms for classification tasks.

## Requirements

- Python 3.13.0
- Key libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

Install dependencies with:
```bash
pip install -r requirements.txt

# Lending Club Loan Analysis - DataFrame Sequence and Processing Overview

This document outlines the sequence of DataFrames used throughout the analysis and the key transformations applied to each. This high-level overview highlights the logical flow from raw data to final model preparation, showcasing data cleaning, feature engineering, and transformations.

## DataFrames and Their Processing Sequence

### 1. `df` - Raw Loan Data
The initial loan data is loaded into the `df` DataFrame. The raw data is cleaned by:
   - Standardising column names to lowercase and replacing spaces with underscores.
   - Handling missing values and inconsistent data types.
   - Removing duplicates to ensure data quality.

### 2. `df_data_dict` - Data Dictionary
The `df_data_dict` DataFrame contains descriptions of each column in the main data. It serves as a reference to interpret variable meanings and structures, helping guide feature categorisation and selection.

### 3. `df_dropped` - Cleaned and Filtered Data
`df_dropped` is created by applying additional transformations to `df`, including:
   - Dropping unnecessary or highly null columns based on preliminary analysis.
   - Filtering records as needed for consistency with project goals.
   - Converting categorical variables to numerical representations where applicable, in preparation for modelling.

### 4. `df_emp_title` - Employment-Specific Data
`df_emp_title` focuses on employment-related fields within the dataset, particularly useful for analysing employment length and titles. Additional cleaning may be applied, such as removing uncommon job titles or grouping similar roles for better interpretability.

### 5. `df_transformed` - Fully Transformed Data
The `df_transformed` DataFrame builds on `df_dropped` with a series of transformations to finalise the dataset for exploratory data analysis (EDA) and modelling:
   - Encoding categorical variables.
   - Normalising or scaling numerical features.
   - Creating logical groupings of variables based on the data dictionary, e.g., grouping by credit history, loan performance, or hardship-related features.
   - Extracting or engineering new features from existing ones, such as date-related fields.

### 6. `cross_tab_df` - Cross-Tabulation for Exploratory Analysis
`cross_tab_df` is used for exploring categorical variables, particularly for understanding distributions and relationships within the data. This DataFrame may also contribute to identifying key predictors of loan performance.

### 7. `defaulted_percentage_df` - Default Rate Analysis
This DataFrame provides a breakdown of loan defaults by category, calculating default percentages across various segments. Insights from this analysis guide feature selection and model target definitions.

### 8. `freq_table` - Frequency Analysis of Categorical Variables
The `freq_table` captures counts and frequencies of categorical values within selected columns. This analysis helps identify dominant categories or balance class distribution, particularly useful for features like loan purpose, home ownership, and employment length.

### 9. `missing_df` and `not_missing_df` - Missing Value Tracking
These DataFrames track missing values in `df`:
   - `missing_df` lists columns with null values, helping prioritise imputation or removal.
   - `not_missing_df` contains data without missing values, enabling comparisons to check if patterns in missingness impact the target variable.

### 10. `vif_data` - Variance Inflation Factor (VIF) Calculation
`vif_data` is used to assess multicollinearity between features. This DataFrame calculates VIF scores, helping remove highly collinear features that may impact model stability and interpretability.

### 11. `uniqueness_df` - Unique Value Analysis
`uniqueness_df` provides insights into the number of unique values per column, highlighting fields with high cardinality or dominant categories that may require further processing, such as grouping or binning.

### 12. `X_train` and `X_test` - Training and Testing Sets
The final modelling datasets are split into `X_train` and `X_test`, with selected features and processed data:
   - `X_train`: Contains the feature set for training the model.
   - `X_test`: Holds the test data to evaluate model performance.
   - These datasets may be scaled and transformed for compatibility with machine learning models.

### 13. `Y` - Target Variable
The `Y` DataFrame holds the target variable for the model, representing the loan status or grouped loan outcome (e.g., default vs. non-default).

### Additional DataFrames for Analysis
Throughout the notebook, various temporary DataFrames may be created for specific tasks such as feature selection (`selected_features`), visualisation, or detailed analysis (`datetime_headers`, `missing_cols`). These are utilised and refined as needed to finalise the data for modelling.

## Summary

This project involves a series of transformations and analyses to prepare the loan data for predictive modelling. Each DataFrame builds on previous steps, ensuring a thorough and logical progression from raw data to fully prepared training and testing sets. These processing steps enable robust feature selection, handling of missing values, encoding, and scaling, laying the groundwork for a reliable model to predict loan approval statuses.

This structure illustrates the comprehensive data science approach followed in this project, demonstrating key skills in data preparation, feature engineering, and analysis.

