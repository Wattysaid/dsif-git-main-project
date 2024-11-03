## 🔍 Data Analysis Process

I structured my analysis by categorising features into Boolean, numerical, and categorical types. For each group, I conducted an in-depth Exploratory Data Analysis (EDA) to understand unique values, distributions, and possible inconsistencies.

### 🧪 Unique Value Counts in Categorical Columns
I started by identifying the number of unique values in each categorical feature, helping me assess the complexity of each column and the need for potential encoding or grouping.

![image](https://github.com/user-attachments/assets/e3a100c0-a8d3-4d5e-aaeb-8de5af6917cd)

This bar chart visualises unique counts across columns like `emp_title`, `title`, and `zip_code`, highlighting `emp_title` with a high count of unique values, which may complicate encoding.

### 📊 Frequency Distribution and Proportion Analysis
To delve deeper into specific categorical features, I analysed `emp_length` through frequency and proportion plots.

![image](https://github.com/user-attachments/assets/d9e1147e-51ae-4b16-9697-128b25a351ff) 
![image](https://github.com/user-attachments/assets/c48ec637-09a0-484d-b703-5c78ba148b15)

- The bar chart shows the distribution across employment lengths, with "10+ years" being the most common.
- The pie chart provides a visual proportion of each category, facilitating insight into the balance of employment lengths within the data.

## Handling Object and Float Features

We have identified the following columns that require conversion or encoding:

### Actions Post-Analysis

#### Convert String to Integer
- **term**: Extract numerical part and convert to integer (keep `36` and `60`).
- **emp_length**: Extract numerical years and convert to integer.

#### Convert String to Float
- **int_rate**: Convert to float after removing any non-numeric characters.
- **revol_util**: Convert to float after removing the "%" symbol.

#### Encode Categorical Values
- **sub_grade**: Use as is or encode if necessary; consider dropping **grade** if redundant.
- **loan_status**: Group or encode based on loan status levels.
- **hardship_loan_status**: Analyze and group similar hardship statuses if logical.

#### Convert to Date/Time Format
- **issue_d**: Convert to date/time for chronological analysis.
- **earliest_cr_line**: Convert to date/time to track the earliest credit history.
- **last_pymnt_d**: Convert to date/time; create separate year and month columns.
- **next_pymnt_d**: Convert to date/time; add year and month columns.
- **last_credit_pull_d**: Convert to date/time for recent credit activity insights.
- **sec_app_earliest_cr_line**: Convert to date/time for secondary applicants’ credit history.
- **hardship_start_date**: Convert to date/time; add year and month columns.
- **hardship_end_date**: Convert to date/time; add year and month columns.
- **payment_plan_start_date**: Convert to date/time; add year and month columns.

#### Remove Non-Analytical or Irrelevant Columns
- **emp_title**: Not relevant for numerical analysis; remove.
- **url**: Non-analytical; remove as it doesn’t contribute to analysis.

#### Evaluate for Categorical Consistency
- **zip_code**: Analyze the first few digits if relevant to extract location-based insights.


### 📉 Boolean Feature Analysis
For Boolean columns, I examined the distribution of True/False values to ensure data completeness and balance.

![image](https://github.com/user-attachments/assets/56bd0d7f-73c1-4706-8996-4bd4f94845ff)
![image](https://github.com/user-attachments/assets/59961217-faf3-45c5-999b-e6f22f7399a3)


In the example above, `earliest_cr_line_missing_clean_kn` is fully populated with "False," indicating no missing values.

### 📐 Numeric Feature Distribution and Outliers
Numeric features like `acc_now_delinq` were analysed using histograms and box plots to understand value distribution and detect outliers.

![image](https://github.com/user-attachments/assets/f5a586ce-0832-42a3-9118-92963bc7a1cc) 

![image](https://github.com/user-attachments/assets/8113f281-e091-419b-b297-9556f05b74f6)

![image](https://github.com/user-attachments/assets/0b965168-581c-4908-99f8-e3d249857c0c)

The histogram shows the skewed distribution of `acc_now_delinq`, while the box plot identifies extreme values as outliers.

### 📅 Date-Time Conversions
To facilitate chronological analysis, I converted columns like `issue_d` and `last_pymnt_d` into date-time formats, creating year and month columns for granular analysis.

### 🧹 Data Cleaning Actions
Based on these insights, I performed data cleaning steps:
- **Converted** strings to integers (e.g., `term`) and floats (e.g., `int_rate`).
- **Encoded** categorical values when necessary.
- **Removed** non-analytical columns like `url` and `emp_title` to streamline the dataset.

### Summary
This combination of statistical reviews and visual tools ensured a thorough understanding of each feature, laying a solid foundation for the subsequent modelling steps.
