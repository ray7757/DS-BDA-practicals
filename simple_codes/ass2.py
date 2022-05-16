#%%
import pandas as pd
import numpy as np

#%%
df=pd.read_csv("C:\\Users\\ADMIN\\Desktop\\data-science_pratice\\StudentsPerformances.csv")
print(df)

#%%
print(df.head(5))

#%%
print(df.describe())

#%%
print(df.isnull().sum())

"""#%%
df['age'][:20]

#%%
df['age']=df['age'].replace(np.NAN,df['age'].mean())
df.isnull().sum()"""

#%%
"""import seaborn as sns
sns.boxplot(df['reading score'])"""
#to find outliers
#print(np.where(df['reading score']<30))

#%%
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

#%%
def UVA_numeric(data):
    var_group = data.columns
    size = len(var_group)
    plt.figure(figsize = (7*size,3), dpi = 400)

    #looping for each variable
    for j,i in enumerate(data.iloc[:,[-3,-1]]):
        

        # calculating descriptives of variable
        mini = data[i].min()
        maxi = data[i].max()
        ran = data[i].max()-data[i].min()
        mean = data[i].mean()
        median = data[i].median()
        st_dev = data[i].std()
        skew = data[i].skew()
        kurt = data[i].kurtosis()

        # calculating points of standard deviation
        points = mean-st_dev, mean+st_dev

        #Plotting the variable with every information
        plt.subplot(1,size,j+1)
        sns.distplot(data[i],hist=True, kde=True)
        sns.lineplot(points, [0,0], color = 'black', label = "std_dev")
        sns.scatterplot([mini,maxi], [0,0], color = 'orange', label = "min/max")
        sns.scatterplot([mean], [0], color = 'red', label = "mean")
        sns.scatterplot([median], [0], color = 'blue', label = "median")
        plt.xlabel('{}'.format(i), fontsize = 20)
        plt.ylabel('density')
        plt.title('std_dev = {}; kurtosis = {};\nskew = {}; range = {}\nmean = {}; median = {}'.format((round(points[0],2),round(points[1],2)),
                                                                                                       round(kurt,2),
                                                                                                       round(skew,2),
                                                                                                       (round(mini,2),round(maxi,2),round(ran,2)),
                                                                                                       round(mean,2),
                                                                                                       round(median,2)))
#%%
UVA_numeric(df)