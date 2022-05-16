
import pandas as pd
#%%
df=pd.read_csv("mallcus.csv")
df.head()
#%%
'''
Provide summary statistics (mean, median, minimum, maximum, standard deviation)
 for a dataset (age, income etc.) with numeric variables grouped by one of the
 qualitative (categorical) variable. For example, if your categorical variable 
 is age groups and quantitative variable is income, then provide summary 
 statistics of income grouped by the age groups. Create a list that contains
 a numeric value for each response to the categorical variable.
'''
#%% summary
df.info()
#%%
print("Summary")
df.describe()
#%%
print("Shape")
df.shape
#%% groupby
df.groupby(("Age"))['Annual Income (k$)'].mean()
df.groupby(("Age"))['Annual Income (k$)'].describe()

#%% 
range=[0,20,30,40,50,60,70] #cat for age
df.groupby(pd.cut(df.Age,range))["Annual Income (k$)"].describe()

'''
Write a Python program to display some basic statistical 
details like percentile, mean, standard deviation etc. of the 
species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’ of iris.csv
 dataset.
'''
#%%
df2=pd.read_csv('Iris.csv')
df2.head()
#%%
setosa=df2['Species']=='Iris-setosa'
setosa=df2[setosa].describe() 
#df.rename(columns = {0:'SepalLengthCm', 1:'SepalWidthCm', 2:'PetalLengthCm', 3:'PetalWidthCm', 4:'Species'}, inplace = True)
#%%
vcolor=df2['Species']=='Iris-versicolor'
vcolor=df2[vcolor].describe()
#%%
df2.size
#%%
df2.shape
df2.info()
df2.describe()
#%%
df2.mean()
#%%
df2.mode()
df2.median()
#%%
df2.SepalLengthCm.std()
df2.SepalWidthCm.std()
#df2.Iris-versicolor.std()