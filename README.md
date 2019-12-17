# Salary Prediction Based on Job Description
# Problem

The goal of this project is to examine a set of job postings with salaries and predict the salary from new job posting.
# File Guide
SalaryPredictionDEA.ipynb- This notebook describes obtaining data, EDA and data preprocessing.

SalaryPrediction.ipynb-This notebook contains data preprocessing, modeling, parameter tuning and predictions.
# Basic data description and EDA
Train dataset has total of 1000000 rows and 8 columns. Six of them are categorical columns and two are numerical columns. There are no missing and duplicate values in the dataset. Following are the descriptions of the columns

# Data preprocessing
There are outliers. I examine the outliers. 25th quartile is 8.5 and 75th quartileis 220.5. I removed the entries with salary below 8.5. Salaries above 75th quartile have reasonable ground to be legitimate data because most of them are C level position with higher degree. Finally, categorical data are converted with One hot encoding.

# Baseline Model
Baseline model is built based on the average salary for industry column and mean squared error(MSE) is calculated 1634.6951926513882 which is very high. So I chose four regression model and they give better result.

# Improved Model
Based on the exploraory data analysis i chose Four regression model and GradientBoosting gives the best result. MSE for gradientBoosting model is 377.45402752571204

# Parameter tuning
GridSearchCV is used to find the best parameters. Best score for the parameters are found to be 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 250 . Using best parameters final MSE is found to be 356.41210502710135.
# Predictions
Final prediction is made based on the best parameters for the chosen model- gradientBoosting
# Feature Importance
Feature importance method is used to find the important feature that influences the predictions. Most important features are identified as jobtype, yearsExperience and milefrommetropolices.

