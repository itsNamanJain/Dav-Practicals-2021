import pandas as pd
from random import sample
from dateutil.parser import parse

df = pd.read_csv("weather.csv")
print("DataFrame :",df.head())

# (a)
df1 = df[['Humidity']].groupby(df['Summary']).mean()
print("(a) Mean of Humidity Series group by Summary series \n:",df1.head(10))

# (b)
df2=df['Formatted Date'].isnull().sum()
print("(b) Filling Missing values :\n",df2)

# (c)
dfC = df.copy()
Month_Year = ['Apr 2020', 'Dec 2013', 'Mar 2017', 'Feb 2009', 'Jun 2001', 'June 2021']
size = len(dfC)
dfC['New_Date'] = [sample(Month_Year,1)[0] for i in range(size)]
df3 = dfC['New_Date'].map(lambda d: parse(d))
print("(c) Year-month string to date conversion\n",df3)

# (d)
def sort_values(dataset, column='Summary', ascending = True):
    return dataset.sort_values(by=column, ascending = ascending)
temp = df.groupby(['Summary', 'Precip Type'])
temp1 = temp.apply(sort_values, column = 'Temperature (C)', ascending = False)
print("(d) Sorted dataset :\n",temp1)

# (e)
df4 = df.groupby(['Precip Type']).count()
print("(e) Splitting dataframe into groups with bin counts\n",df4)