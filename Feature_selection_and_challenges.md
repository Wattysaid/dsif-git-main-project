# 🔍 Feature Selection for Loan Default Prediction

### 📋 Feature Selection Summary

The results of the RFE excercise are captured below. Before getting to these results I first reviewed the data dictionary. I created logical groupings for the data then created two groups pre and post hardship. I created this grouping off the back of the data dictionary. I then proceeded to evaluate the data I grouped under the pre-hardship category.

---

### 🗂️ RFE Features by logical grouping (grouping and pre-hardship)

- **Credit History**:
  - `mo_sin_old_il_acct`
  - `mo_sin_old_rev_tl_op`

- **Current Debt and Payment Behaviours**:
  - `bc_open_to_buy`
  - `revol_bal`
  - `total_bal_ex_mort`

- **Employment**:
  - `annual_inc`

- **Loan Performance**:
  - `total_rec_int`
  - `total_rec_late_fee`
  - `total_rec_prncp`

---

### 🔄 Features in Pre-Hardship Fields

The following RFE-selected features are also part of the pre-hardship fields, meaning they capture borrower data available prior to any hardship events:

- `annual_inc`
- `bc_open_to_buy`
- `dti`
- `il_util`
- `installment`
- `mo_sin_old_il_acct`
- `mo_sin_old_rev_tl_op`
- `mo_sin_rcnt_rev_tl_op`
- `mo_sin_rcnt_tl`
- `mths_since_rcnt_il`
- `mths_since_recent_bc`
- `num_il_tl`
- `revol_bal`
- `total_bal_ex_mort`
- `total_il_high_credit_limit`
- `total_rec_int`
- `total_rec_late_fee`
- `total_rec_prncp`

## 📋 Overview

To effectively build a model for predicting loan defaults, I first reviewed the data dictionary and organised features into logical groups based on their financial and behavioural relevance. This grouping was essential for gaining insights into various feature categories, ensuring a structured approach for feature engineering and selection.

## 🗂️ Feature Groups

Using domain knowledge and insights from the Lending Club dataset, I categorised the features into groups. This structured classification laid the foundation for targeted feature selection, particularly for post-ML analysis. These groups include:

- **Credit History**: Tracks historical credit behaviour, including credit line age and FICO scores.
  - *Examples*: `earliest_cr_line`, `fico_range_high`, `mo_sin_old_il_acct`

- **Current Debt and Payment Behaviours**: Reflects current credit usage and payment patterns.
  - *Examples*: `acc_now_delinq`, `bc_open_to_buy`, `revol_bal`

- **Employment**: Includes income and employment information.
  - *Examples*: `emp_length`, `annual_inc`

- **Credit Inquiries**: Records the frequency and recency of credit inquiries.
  - *Examples*: `inq_last_6mths`, `num_tl_op_past_12m`

- **Loan Application Information**: Basic application details like loan amount and purpose.
  - *Examples*: `loan_amnt`, `int_rate`, `purpose`

- **Hardship and Settlement Information**: Records any instances of hardship or debt settlement.
  - *Examples*: `hardship_flag`, `settlement_status`, `settlement_date`

- **Co-Borrower Information**: Contains data related to joint applications and co-borrowers.
  - *Examples*: `annual_inc_joint`, `dti_joint`

- **Loan Performance**: Tracks the performance of the loan, including payment history.
  - *Examples*: `total_pymnt`, `total_rec_int`, `recoveries`

These groupings allowed me to systematically explore feature importance within each category and evaluate their relevance to loan default predictions.

## ⚙️ Pre- and Post-Hardship Fields

After reviewing the feature groups, I divided features further into two main sets based on their relation to hardship status:

- **Pre-Hardship Fields**: These features capture information available at loan origination or during regular servicing, before any hardship events.
  - *Examples*: `acc_now_delinq`, `annual_inc`, `fico_range_high`, `loan_amnt`

- **Post-Hardship Fields**: These features are related to financial hardships or debt settlements after loan issuance.
  - *Examples*: `hardship_flag`, `settlement_date`, `hardship_start_date`

I selected the pre-hardship fields as the initial draft feature set to avoid bias from post-hardship features that may directly indicate defaults.

## 🔄 Recursive Feature Elimination (RFE)

To further refine feature selection, I applied Recursive Feature Elimination (RFE). This technique helped to systematically reduce the feature set while retaining predictive power by iteratively removing the least impactful features. My goal was to simplify the model and minimise the risk of data leakage by ensuring each feature contributed meaningfully to loan default predictions.

### 📑 Final Selected Features

After running RFE, the following features were selected, capturing key aspects of income, credit history, and payment behaviours:

- `annual_inc`
- `bc_open_to_buy`
- `dti`
- `il_util`
- `installment`
- `mo_sin_old_il_acct`
- `mo_sin_old_rev_tl_op`
- `mo_sin_rcnt_rev_tl_op`
- `mo_sin_rcnt_tl`
- `mths_since_rcnt_il`
- `mths_since_recent_bc`
- `num_il_tl`
- `revol_bal`
- `total_bal_ex_mort`
- `total_il_high_credit_limit`
- `total_rec_int`
- `total_rec_late_fee`
- `total_rec_prncp`
- `int_rate_kn`
- `revol_util_kn`
- `issue_d_year_kn`
- `issue_d_month_kn`
- `earliest_cr_line_year_kn`

---

These selected features provide a comprehensive view of the borrower’s financial behaviour and loan performance, making them highly valuable for the predictive model. By focusing on pre-hardship features, I aimed to avoid data leakage and ensure that the model captures patterns relevant to default risk assessment.

These RFE-selected features offer a well-rounded view of borrower behaviour and financial capacity, while avoiding excessive complexity. With these features, the model is equipped to identify default risks effectively while remaining interpretable and robust.
