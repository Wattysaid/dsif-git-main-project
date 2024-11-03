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

### Handling Object and Float Features

Several columns required type conversion or encoding after analysis:

#### Actions Post-Analysis

- **Convert String to Integer**: `term` and `emp_length`
- **Convert String to Float**: `int_rate` and `revol_util`
- **Encode Categorical Values**: `sub_grade`, `loan_status`, `hardship_loan_status`
- **Convert to Date/Time**: `issue_d`, `earliest_cr_line`, `last_pymnt_d`, and others
- **Remove Irrelevant Columns**: `emp_title`, `url`
- **Evaluate Categorical Consistency**: `zip_code`

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

### 📅 Date-Time Conversions
For chronological insights, I converted columns like `issue_d` and `last_pymnt_d` to date-time formats, generating year and month columns for added granularity.

### 🧹 Data Cleaning Actions
Based on the findings:
- **Strings were converted** to integers (e.g., `term`) and floats (e.g., `int_rate`).
- **Categorical values were encoded** where appropriate.
- **Non-analytical columns were removed** to streamline the dataset.

### Summary
This mix of statistical evaluations and visualisations provided a clear understanding of each feature, establishing a robust foundation for subsequent modelling.
