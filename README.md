# Lending Club Loan Analysis - ELVTR Data Science Course Project

This project is part of the ELVTR Data Science course, designed to demonstrate the application of data science skills in a financial context. The primary goal is to analyze and model a dataset of loan applications to predict loan approval statuses.

## Project Objectives

1. **Data Cleaning and Preprocessing**: 
   - Handle missing values and inconsistent data types.
   - Remove duplicate entries, standardize, and normalize features.
2. **Feature Engineering and Selection**:
   - Categorize features into logical groups for better interpretability (e.g., credit history, employment information, loan performance).
   - Filter relevant features for modeling.
3. **Exploratory Data Analysis (EDA)**:
   - Perform statistical analysis and visualization to uncover trends and insights.
4. **Predictive Modeling**:
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
   - Visualize data distributions and correlations between features.
   - Identify key insights about loan performance and borrower profiles.
5. **Modeling**:
   - Prepare data for modeling with selected features.
   - Implement and evaluate models based on chosen evaluation metrics.

## Key Concepts Demonstrated

- **Data Cleaning**: Importance of preprocessing to ensure data quality.
- **Feature Selection**: Methods to retain meaningful variables for modeling.
- **Exploratory Analysis**: Using visualizations to understand trends.
- **Predictive Modeling**: Application of machine learning algorithms for classification tasks.

## Requirements

- Python 3.13.0
- Key libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

Install dependencies with:
```bash
pip install -r requirements.txt
