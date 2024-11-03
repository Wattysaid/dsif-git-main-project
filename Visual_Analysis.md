## 🔍 Data Analysis Process

I organised the analysis by categorising features into Boolean, numerical, and categorical types, performing an Exploratory Data Analysis (EDA) for each group to understand unique values, distributions, and any potential inconsistencies.

### 🧪 Unique Value Counts in Categorical Columns
I began by identifying the number of unique values in categorical features to assess column complexity and determine if encoding or grouping was necessary.

![image](https://github.com/user-attachments/assets/235467ba-f7f7-4479-9c2f-111df893bd71)

![image](https://github.com/user-attachments/assets/64c1a4f9-b8b2-4279-86ff-56bb8e91fca2)

The bar chart shows the unique counts across our categorical and numerical lists. This helps us determine which of our features form wither list is worth investigating. High variability in the category list won't be included in the graphical analysis but instead evaluated based on numerical tables, this is the opposite approach for numerical values in which case I've analysed the columns with the highest amount of variability as these will be more indicative for predictions.

### 📊 Frequency Distribution and Proportion Analysis
To further investigate, I used frequency and proportion charts on `emp_length`.

![image](https://github.com/user-attachments/assets/d9e1147e-51ae-4b16-9697-128b25a351ff) 

![image](https://github.com/user-attachments/assets/c48ec637-09a0-484d-b703-5c78ba148b15)

- The bar chart visualises the spread of employment lengths, with "10+ years" as the most frequent.
- The pie chart illustrates each category's share, providing a balanced perspective of employment lengths within the dataset.

### 📉 Boolean Feature Analysis
For Boolean features, I reviewed True/False distributions to ensure data completeness.

![image](https://github.com/user-attachments/assets/56bd0d7f-73c1-4706-8996-4bd4f94845ff)

![image](https://github.com/user-attachments/assets/59961217-faf3-45c5-999b-e6f22f7399a3)

The distribution of `earliest_cr_line_missing_clean_kn` indicates full completeness, with all values marked "False."

### 📐 Numeric Feature Distribution and Outliers
Numeric features, like `acc_now_delinq`, were examined using histograms and box plots to uncover value distribution and detect outliers.

![image](https://github.com/user-attachments/assets/6c1f4435-ea95-46f0-9d86-9ece0212189f)

![image](https://github.com/user-attachments/assets/6c5f3e35-cd51-4c23-99c7-5e6a289c9fc0)

![image](https://github.com/user-attachments/assets/f27583e8-686d-4b65-bd78-66ad3dc2b131)

The histogram highlights a skewed distribution in `acc_now_delinq`, while the box plot identifies several outliers.

### 🧹 Data Cleaning Actions

We have identified the following columns that require conversion or encoding:

#### Actions Post-Analysis

##### Convert String to Integer
- `term`: Extract numerical part and convert to integer (keep `36` and `60`).
- `emp_length`: Extract numerical years and convert to integer.

##### Convert String to Float
- **int_rate**: Convert to float after removing any non-numeric characters.
- **revol_util**: Convert to float after removing the "%" symbol.

##### Encode Categorical Values
- **sub_grade**: Use as is or encode if necessary; consider dropping **grade** if redundant.
- **loan_status**: Group or encode based on loan status levels.
- **hardship_loan_status**: Analyze and group similar hardship statuses if logical.

##### Convert to Date/Time Format
- **issue_d**: Convert to date/time for chronological analysis.
- **earliest_cr_line**: Convert to date/time to track the earliest credit history.
- **last_pymnt_d**: Convert to date/time; create separate year and month columns.
- **next_pymnt_d**: Convert to date/time; add year and month columns.
- **last_credit_pull_d**: Convert to date/time for recent credit activity insights.
- **sec_app_earliest_cr_line**: Convert to date/time for secondary applicants’ credit history.
- **hardship_start_date**: Convert to date/time; add year and month columns.
- **hardship_end_date**: Convert to date/time; add year and month columns.
- **payment_plan_start_date**: Convert to date/time; add year and month columns.

##### Remove Non-Analytical or Irrelevant Columns
- **emp_title**: Not relevant for numerical analysis; remove.
- **url**: Non-analytical; remove as it doesn’t contribute to analysis.

##### Evaluate for Categorical Consistency
- **zip_code**: Analyze the first few digits if relevant to extract location-based insights.


### Summary
This mix of statistical evaluations and visualisations provided a clear understanding of each feature, establishing a robust foundation for subsequent modelling.
