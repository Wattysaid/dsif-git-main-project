# Reports

## 🔗 Navigation Menu

- 📘 [README](https://github.com/Wattysaid/dsif-git-main-project/blob/main/README.md)
- 📄 [Overview of DataFrame Sequence and Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/DataFrame_Sequence_and_Processing_Overview.md)
- 📊 [ELVTR Report](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ELVTR_report.md)
- 🔍 [Feature Selection and Challenges](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Feature_selection_and_challenges.md)
- 📑 [Key Lists for Data Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Key_Lists_for_Data_Processing.md)
- 🤖 [ML Models and Results](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ML_models_and_results.md)
- 🧠 [Neural Network Selection](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Neural_Network_selection.md)
- ⚙️ [Understanding Feature Impact](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Understanding_feature_impact.md)
- 📈 [Visual Analysis](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Visual_Analysis.md)

This document contains all image files from the reports directory.

# Reports

This document contains all image files from the reports directory.

Let's take a quick look at our Y variable (`loan_status`) and get a feel for some obvious view points e.g. loan purpose, states in which loan default are higher, etc. This is largely subjective but could lead to some quick wins or cleaning insight.

Our first image is a grouped view of `loan_status` by `loan_purpose` showing us that the marjority of loans are for debt conslidation, credit card consumption and home improvement.

![image_cell165_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell165_output0.png)

Our second image shows us the grouped `loan_status` by `verification_status`.

![image_cell167_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell167_output0.png)

Below we can see the number of loans by state. Let's take a closer look.

![image_cell170_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell170_output0.png)

I've split the data to gain better insight into the grouped `loan_status` by state. Here we can see that majority of loans are spread across 4 states but more importantly that there is a large ratio descrepancy when looking at the ratio of defaulted loans when compared to the total loan appcliations in various states. Let's pull a cross table to confirm our visual analysis.

![image_cell171_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell171_output0.png)

# Data Unique value check

Here I'm looking at the categorical distribution of our data. Too many values within the data set make for poor visuals and should be grouped accordingly. This allows us to quickly notice one of these grouping options i.e. by emp_title. This could, for example, be grouped by equivalent hierarchical roles.

![image_cell108_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell108_output1.png)

Here we can see an extension of the aforementioned excercise. Essentially including additional values previously excluded. This allowed me to loop through our lists and equally display the numerical data.

![image_cell110_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell110_output1.png)

Through a similar lens I'm looking for numerical values that allow for deeper insight into the values we have. Here we can see that the first 15 numerical values contain a large portoin of the data with various levels of value counts. For example, visually analysing some of our data with too few variations won't contribute to benefitcing results in our ML analysis.

![image_cell110_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell110_output3.png)

# Categorical data analysis

Here we're looking at the key points surrounding our categorical data. I'm looking for data I can encode, group into more meaningful buckets, poor data, and possible features to include in our analysis.

In this first image we can see that `emp_length` can be changed to a int. We'll take action later by changing the data type to int and removeing the origninal column from our `new_features` list and the df_dropped.

![image_cell112_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell112_output1.png)

This is our Y variable that will later be used as the prediction value (`loan_status`). We'll group this field to simplify the output.

![image_cell112_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell112_output3.png)

This next view shows us the `sub_grade` for loans. This is arguably too granular and we'll remove this column, and leverage the `grade` column only. However, before doing so we'll check bot `sub_grade` and `grade` against our `loan_status` feature.

![image_cell112_output5.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell112_output5.png)

Here we can see another field that we can transform into a int data type value. Considering the low variation we'll could equally look at dropping this altogether. Let's flag this one for further analysis later on and see how this impacts the overall data.

![image_cell112_output7.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell112_output7.png)

# Boolean data analysis

Here we're looking for one value items, these won't add any meaningful insight and can be removed. However, multiple boolean values could be meaningful when matched with other boolean values. In this assignment we've opted for creating boolean indicators for missing fields. Essentially if a value is missing we've created a boolean marker (1 = Missing data point, 0 = Not missing a data point). Due to the nature of our data the fact that salary figures, or partnership situations are missing could provide insight. We will test this theory later.

![image_cell156_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output1.png)
![image_cell156_output11.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output11.png)
![image_cell156_output13.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output13.png)
![image_cell156_output15.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output15.png)
![image_cell156_output17.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output17.png)
![image_cell156_output19.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output19.png)
![image_cell156_output21.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output21.png)
![image_cell156_output23.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output23.png)
![image_cell156_output25.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output25.png)
![image_cell156_output27.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output27.png)
![image_cell156_output29.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output29.png)
![image_cell156_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output3.png)
![image_cell156_output31.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output31.png)
![image_cell156_output33.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output33.png)
![image_cell156_output35.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output35.png)
![image_cell156_output37.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output37.png)
![image_cell156_output5.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output5.png)
![image_cell156_output7.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output7.png)
![image_cell156_output9.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell156_output9.png)

# Numerical data analysis

Here we're looking for distribution and missing value data. Does our numerical data set contain sufficient variation to be of predictive value? We can safely exclude any numerical data that is comprised of unique values, or too small ranges/variation.

![image_cell162_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output1.png)
![image_cell162_output10.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output10.png)
![image_cell162_output13.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output13.png)
![image_cell162_output16.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output16.png)
![image_cell162_output19.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output19.png)
![image_cell162_output22.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output22.png)
![image_cell162_output25.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output25.png)
![image_cell162_output28.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output28.png)
![image_cell162_output31.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output31.png)
![image_cell162_output34.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output34.png)
![image_cell162_output37.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output37.png)
![image_cell162_output4.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output4.png)
![image_cell162_output40.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output40.png)
![image_cell162_output43.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output43.png)
![image_cell162_output46.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output46.png)
![image_cell162_output49.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output49.png)
![image_cell162_output52.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output52.png)
![image_cell162_output55.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output55.png)
![image_cell162_output58.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output58.png)
![image_cell162_output61.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output61.png)
![image_cell162_output64.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output64.png)
![image_cell162_output67.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output67.png)
![image_cell162_output7.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output7.png)
![image_cell162_output70.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output70.png)
![image_cell162_output73.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output73.png)
![image_cell162_output76.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output76.png)
![image_cell162_output79.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell162_output79.png)
![image_cell237_output11.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output11.png)
![image_cell237_output14.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output14.png)
![image_cell237_output15.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output15.png)
![image_cell237_output17.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output17.png)
![image_cell237_output2.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output2.png)
![image_cell237_output20.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output20.png)
![image_cell237_output21.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output21.png)
![image_cell237_output23.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output23.png)
![image_cell237_output26.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output26.png)
![image_cell237_output27.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output27.png)
![image_cell237_output29.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output29.png)
![image_cell237_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output3.png)
![image_cell237_output32.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output32.png)
![image_cell237_output33.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output33.png)
![image_cell237_output35.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output35.png)
![image_cell237_output5.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output5.png)
![image_cell237_output8.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output8.png)
![image_cell237_output9.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell237_output9.png)
![image_cell242_output11.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output11.png)
![image_cell242_output14.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output14.png)
![image_cell242_output15.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output15.png)
![image_cell242_output17.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output17.png)
![image_cell242_output2.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output2.png)
![image_cell242_output20.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output20.png)
![image_cell242_output21.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output21.png)
![image_cell242_output23.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output23.png)
![image_cell242_output26.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output26.png)
![image_cell242_output27.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output27.png)
![image_cell242_output29.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output29.png)
![image_cell242_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output3.png)
![image_cell242_output32.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output32.png)
![image_cell242_output33.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output33.png)
![image_cell242_output35.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output35.png)
![image_cell242_output5.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output5.png)
![image_cell242_output8.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output8.png)
![image_cell242_output9.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell242_output9.png)
![image_cell276_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell276_output0.png)
![image_cell291_output2.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell291_output2.png)
![image_cell293_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell293_output1.png)
![image_cell295_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell295_output1.png)
![image_cell302_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell302_output1.png)
![image_cell303_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell303_output1.png)
![image_cell304_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell304_output1.png)
![image_cell305_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell305_output1.png)
![image_cell306_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell306_output1.png)
![image_cell309_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell309_output1.png)
![image_cell310_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell310_output1.png)
![image_cell316_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell316_output1.png)
![image_cell42_output2.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell42_output2.png)
![image_cell42_output3.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell42_output3.png)
![image_cell55_output1.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell55_output1.png)
![image_cell75_output0.png](https://raw.githubusercontent.com/Wattysaid/dsif-git-main-project/main/elvtr_main_project/reports/image_cell75_output0.png)
