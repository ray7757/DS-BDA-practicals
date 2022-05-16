import pandas as pd
#import seaborn as sns
#%%
df=pd.read_csv("studp.csv")
df.head()
#%%
'''                                
Scan all variables for missing val and deal with them
'''
df["reading score"].isnull().sum()
df.isnull().sum()
#%%
df["reading score"].fillna(df["reading score"].mean())
df.fillna(method="bfill")#fills miss val backward
#%%
#OUTERLIERS
import seaborn as sns
sns.boxplot(df["reading score"])
df=df[~(df['reading score']<=30)]
#%%
sns.boxplot(df["writing score"])
df=df[~(df['writing score']<25)]
#%%
#data transformation

#%%
sns.histplot(df['reading score'])
#%%
#data transform normalization

from scipy import  stats
nordata=stats.boxcox(df['reading score'])
#fig,ax=plt.subplot(1,2,figsize=(15,3))
sns.histplot(nordata[0])