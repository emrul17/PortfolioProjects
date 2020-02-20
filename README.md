# Salary Prediction Based on Job Description
# Problem

Offering an appropriate salary is aspect of job posting for employeers. Beause decent salary offer can bring the best talent to the team. It is always difficult to predict the right salary for a particular position. The goal of this project is to examine a set of job postings with salaries and predict the salary from new job posting.

# Data collection 
Train dataset has total of 1000000 rows and 8 columns. Following are the deatails of data:
jobId-jobId is the unique id for each job posting.
companyId- There are total of 63 unique company id, representing each company.
jobType-jobType column represents individual job type. Such as ECO, manager, Vice_precident, CFO etc.
degree-degree column refers to 5 different types of degree employee has. They are doctoral, masters, bachelor, High school and None.
major-This represents what major they have. For example, Physics, chemistry, biology, engineering, business etc.
industry -industry column represents about different types of industries like Web, financical service, health, education, service, oil and auto.
yearsExperience- This difines how many years of experiences employee has
milesFromMetropolis-This indicates how far the job location from the metropliton area.
Six of them are categorical columns and two are numerical columns. There are no missing and duplicate values in the dataset. Following are the descriptions of the columns

# File Guide
SalaryPredictionDEA.ipynb- This notebook describes obtaining data, EDA and data preprocessing.

SalaryPrediction.ipynb-This notebook contains data preprocessing, modeling, parameter tuning and predictions.

# Data preprocessing

As a part of data cleaning I have impelemented following steps:

Missing value handling: Luckily there is no missing values.

Outliers: From the box plot, it is clear that salary below 8.5K is an outliers. So I removed this data point. Salaries above 75th quartile have reasonable ground to be legitimate data because most of them are C level position with higher degree. From EDA, It is seen that, Highly paid industries are OIL and FINANCE and lowest paid is Education. Similarly, CEO is paid highest followed by CTO, CFO, Vice_president, Senior, Juior and Janitar. For degree, it is seen that salaries increases according to their level of education. However, Average salary for all majors is almost same. None degrees are paid less than average. 
![Salary](https://user-images.githubusercontent.com/33338872/74778437-30aa6480-5261-11ea-9076-887f5c77b012.jpg)

I used label encoding to convert the categorical data into numerical.
# Exploratory Data Analysis
Looking at the Box plot, average salary for higher educated people are higher compared to those who have low degree. Similary C-level positions are paid higher salary. However, average salary for all majors are pretty much same. For industry, Oil and finance are highly paid industry whereas eaducation is low paying industry. 
![jobType](https://user-images.githubusercontent.com/33338872/74778477-491a7f00-5261-11ea-9936-848ada21bbab.jpg)
![degree](https://user-images.githubusercontent.com/33338872/74778499-55064100-5261-11ea-83fc-70059be92881.jpg)
![major](https://user-images.githubusercontent.com/33338872/74778511-5899c800-5261-11ea-9f0b-3e31859a86f0.jpg)
![cat_plot](https://user-images.githubusercontent.com/33338872/74778518-5a638b80-5261-11ea-8d29-9a42a6ab0820.jpg)

From numerical plot, It is found that, Salary Increase linearly with yearsExperiences wheras salary decreaes with increase milesFromMetroplis. 
![yearsExperience](https://user-images.githubusercontent.com/33338872/74958072-0c1fcb00-53ce-11ea-878f-579fce868813.jpg)
![milesFromMetropolis](https://user-images.githubusercontent.com/33338872/74958080-0e822500-53ce-11ea-99e5-86f562e747f7.jpg)

# Modeling
Baseline model is built based on the average salary for industry column and mean squared error(MSE) is calculated 1634.6951926513882 which is very high. 
Based on the exploraory data analysis i chose Four regression models(LinearRegression, RandomForestRegressor, GradientBoostingRegressor, XGBRegressor) and compared the scores. GradientBoosting gives the best result. MSE for gradientBoosting model is 377.45402752571204. This result is found for default parameters. By applying parameter tuning method we can find the best parameters. 

# Parameter tuning and predictions
GridSearchCV is used to find the best parameters. Best score for the parameters are found to be 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 250 . Using best parameters final MSE is found to be 356.41210502710135.
Final prediction is made based on the best parameters for the chosen model- gradientBoosting

# Feature Importance
Feature importance method is used to find the important features that influences the predictions. Most important features are identified as jobtype, yearsExperience and milefrommetropolices.

