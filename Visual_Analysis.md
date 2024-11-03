### 🔍 Data Analysis Process

I structured my analysis by categorising features into Boolean, numerical, and categorical types. For each group, I conducted an in-depth Exploratory Data Analysis (EDA) to understand unique values, distributions, and possible inconsistencies.

#### 🧪 Unique Value Counts in Categorical Columns
I started by identifying the number of unique values in each categorical feature, helping me assess the complexity of each column and the need for potential encoding or grouping.

![image](https://github.com/user-attachments/assets/e3a100c0-a8d3-4d5e-aaeb-8de5af6917cd)

This bar chart visualises unique counts across columns like `emp_title`, `title`, and `zip_code`, highlighting `emp_title` with a high count of unique values, which may complicate encoding.

#### 📊 Frequency Distribution and Proportion Analysis
To delve deeper into specific categorical features, I analysed `emp_length` through frequency and proportion plots.

![image](https://github.com/user-attachments/assets/d9e1147e-51ae-4b16-9697-128b25a351ff) | ![image](https://github.com/user-attachments/assets/c48ec637-09a0-484d-b703-5c78ba148b15)

- The bar chart shows the distribution across employment lengths, with "10+ years" being the most common.
- The pie chart provides a visual proportion of each category, facilitating insight into the balance of employment lengths within the data.

#### 📉 Boolean Feature Analysis
For Boolean columns, I examined the distribution of True/False values to ensure data completeness and balance.

![Boolean Distribution Example](boolean_distribution.png)

In the example above, `earliest_cr_line_missing_clean_kn` is fully populated with "False," indicating no missing values.

#### 📐 Numeric Feature Distribution and Outliers
Numeric features like `acc_now_delinq` were analysed using histograms and box plots to understand value distribution and detect outliers.

![Numeric Distribution and Outliers](numeric_distribution_outliers.png)

The histogram shows the skewed distribution of `acc_now_delinq`, while the box plot identifies extreme values as outliers.

#### 📅 Date-Time Conversions
To facilitate chronological analysis, I converted columns like `issue_d` and `last_pymnt_d` into date-time formats, creating year and month columns for granular analysis.

#### 🧹 Data Cleaning Actions
Based on these insights, I performed data cleaning steps:
- **Converted** strings to integers (e.g., `term`) and floats (e.g., `int_rate`).
- **Encoded** categorical values when necessary.
- **Removed** non-analytical columns like `url` and `emp_title` to streamline the dataset.

### Summary
This combination of statistical reviews and visual tools ensured a thorough understanding of each feature, laying a solid foundation for the subsequent modelling steps.
