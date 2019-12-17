# Salary Prediction Based on Job Description
# Problem

The goal of this project is to examine a set of job postings with salaries and predict the salary from new job posting.
# File Guide
SalaryPredictionDEA.ipynb- This notebook describes obtaining data, EDA and data preprocessing.

SalaryPrediction.ipynb-This notebook contains data preprocessing, modeling, parameter tuning and predictions.
# Basic data description and EDA
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

# Data preprocessing
I examine the outliers of salary column. 25th quartile is 8.5k and 75th quartileis 220.5k. I removed the entries with salary below 8.5. Salaries above 75th quartile have reasonable ground to be legitimate data because most of them are C level position with higher degree. From EDA, It is seen that, Highly paid industries are OIL and FINANCE and lowest paid is Education. Similarly, CEO is paid highest followed by CTO, CFO, Vice_president, Senior, Juior and Janitar. For degree, it is seen that salaries increases according to their level of education. However, Average salary for all majors is almost same. None degrees are paid less than average. 

salary Increase linearly with yearsExperiences wheras salary decreaes with increase milesFromMetroplis.

# Baseline Model
Baseline model is built based on the average salary for industry column and mean squared error(MSE) is calculated 1634.6951926513882 which is very high. Different ML models can be tested to reduce the MSE

# Improved Model
Based on the exploraory data analysis i chose Four regression models(LinearRegression, RandomForestRegressor, GradientBoostingRegressor, XGBRegressor and compared the score. GradientBoosting gives the best result. MSE for gradientBoosting model is 377.45402752571204

# Parameter tuning
GridSearchCV is used to find the best parameters. Best score for the parameters are found to be 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 250 . Using best parameters final MSE is found to be 356.41210502710135.
# Predictions
Final prediction is made based on the best parameters for the chosen model- gradientBoosting
# Feature Importance
Feature importance method is used to find the important feature that influences the predictions. Most important features are identified as jobtype, yearsExperience and milefrommetropolices.

