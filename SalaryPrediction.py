
# coding: utf-8

# # Salary Prediction EDA
# This is a data of job postings with salaries and our task is to make a prediction of future salaries based on job posting.
# In this notebook I will explain exploratory data analysis as depth as possible. This notebook also will make necessary comment on features.

# Necessary libraries

# In[33]:


import pandas as pd
import sklearn as sk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Personal Information
__author__ = "Emrul Hasan"
__email__ = "emrul.phy@gmail.com"


# Loading data

# In[34]:


#load the data into a Pandas dataframe
df_train=pd.read_csv('train_features.csv')
df_test=pd.read_csv('test_features.csv')
df_salary=pd.read_csv('train_salaries.csv')


# Examine the data

# In[35]:


df_train.head()


# In[36]:


df_salary.head()


# In[37]:


df_test.head()


# In[38]:


df_train.shape


# In[39]:


df_salary.shape


# In[40]:


df_test.shape


# By having a look at the datasets, it is obvious that entries and columns for train and salary datasets are same. But test dataset has diffient number of columns. So lets merge the target dataset to traindataset. Since the job id column is same for both train and salary data,so we can merge on that.

# In[70]:


train_data=pd.merge(df_train, df_salary,on='jobId')


# In[42]:


train_data.shape


# In[43]:


train_data.info()


# In[44]:


train_data.columns


# In[45]:


train_data.describe(include=np.number)


# In[46]:


train_data.describe(include='O')


# Cleaning data

# In[47]:


# duplicate checks
train_data.duplicated().sum()


# In[48]:


# checking missing values
train_data.isnull().sum()


# There is no missing and duplicate values.

# In[49]:


plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
sns.boxplot(train_data.salary)

plt.subplot(1,2,2)
sns.distplot(train_data.salary, bins=20)

plt.show()


# It is clear that there are outliers. Let's handle the outliers

# In[50]:


stat=train_data.salary.describe()
IQR=stat['75%']-stat['25%']
upper=stat['75%']+1.5*IQR
lower=stat['25%']-1.5*IQR

print('The upper and lower bounds for outliers are {} and {}'.format(upper,lower))


# In[51]:


# check the potential suspicious outliers below the lower boun
train_data[train_data.salary<8.5]


# In[52]:


outliers_low=train_data[train_data.salary<8.5]
outliers_up=train_data[train_data.salary>220.5]
# number of outliers
train_data.loc[train_data.salary>220.5,'jobType'].value_counts()


# In[53]:


# check the potential suspicious outliers above the upper bound
train_data[(train_data.salary>220.5) & (train_data.jobType=='JUNIOR')]


# These entries with zero salary are not realistic. We are confident that these are missing or corupted data and should be removed from training data set.
# 
# The high salary potential outliers appear to be legitimate data. Most of the roles are c-level junior position. As it is seen that the employes have advanced degrees and the companies like oil and finance well known for high salaries, it is expected the the data are realistics.

# In[54]:


# remove the data with zero salaries
train_data=train_data[train_data.salary>8.5]


# In[55]:


def plot_feature(df,col):
    """
    Make a plot for all features
    left, distribution of features on sample
    right, relationship between salary and feature
    """
    plt.figure(figsize=(14,6))
    plt.subplot(1,2,1)
    if df[col].dtype=='int64':
        df[col].value_counts().sort_index().plot()
    else:
        # change the categorical variable to category and order them by their mean salary in each category.
        
        mean=df.groupby(col)['salary'].mean()
        df[col]=df[col].astype('category')
        levels=mean.sort_values().index.tolist()
        df[col].cat.reorder_categories(levels,inplace=True)
        df[col].value_counts().plot()
        
    plt.xticks(rotation=45)
    plt.xlabel(col)
    plt.ylabel('Counts')
    plt.subplot(1,2,2)
        
    if df[col].astype=='int64' or col=='companyId':
        # plot the mean salary for each salary and fill between(mean-std, mean+std)
        mean=df.groupby(col)['salary'].mean()
        std=df.groupby(col)['salary'].std()
        mean.plot()
        
        plt.fill_between(range(len(std.index)),mean.values-std.values, mean.values+std.values, alpha=0.1)

        
    else:
        sns.boxplot(x=col, y='salary', data=df)
        
    plt.xticks(rotation=45)
    plt.ylabel('salary')
    plt.show()


# In[56]:


plot_feature(train_data,'companyId')


# In[57]:


plot_feature(train_data,'jobType')


# In[58]:


plot_feature(train_data,'major')


# In[59]:


plot_feature(train_data, 'industry')


# In[60]:


plot_feature(train_data, 'degree')


# Convert the categorical data to numerical data

# In[66]:


def encode_label(df, col):
    #encode the categories using average salary for each category to replace label
    cat_dict ={}
    cats = df[col].cat.categories.tolist()
    for cat in cats:
        cat_dict[cat] = df[df[col] == cat]['salary'].mean()   
    df[col] = df[col].map(cat_dict)


# In[67]:


for col in train_data.columns:
    if train_data[col].dtype.name == "category":
        encode_label(train_data, col)


# In[69]:


train_data.head()


# In[68]:


fig=plt.figure(figsize=(14,10))
features=['companyId', 'jobType', 'degree', 'major', 'industry','yearsExperience', 'milesFromMetropolis']
sns.heatmap(train_data[features + ['salary']].corr(), cmap='Blues', annot=True)
plt.xticks(rotation=45)
plt.show()

