import pandas as pd
import numpy as np
data1 = [["Naman","Nov 5 2021 12:00 PM",40],["Heena","Nov 5 2021 12:05 PM",50],["Ram","Nov 5 2021 12:10 PM",30],["Geeta","Nov 5 2021 12:02 PM",40],["Sourabh","Nov 5 2021 12:12 PM",50],["Monty","Nov 5 2021 12:20 PM",30]]
df1 = pd.DataFrame(data1, columns = ['Name', 'Time_of_Joining','Duration'])
data2 = [["Sunita","Nov 5 2021 12:01 PM",30],["Ramesh","Nov 5 2021 12:08 PM",40],["Naman","Nov 5 2021 12:05 PM",30],["Monty","Nov 5 2021 12:10 PM",30],["Rajni","Nov 5 2021 12:02 PM",50],["Ram","Nov 5 2021 12:07 PM",40]]
df2 = pd.DataFrame(data2, columns = ['Name', 'Time_of_Joining','Duration'])

# (a)
df3 = pd.merge(df1,df2,on="Name")
print("(a) Name of Students attended workshop both days\n",df3["Name"])

# (b)
df4 = np.union1d(df1['Name'], df2['Name'])
print("(b) Name of Students attended workshop either days\n",df4)

# (c)
df5 = pd.merge(df1, df2, left_index = True, right_index = True)
print("(c) Merging dataframe row-wise",df5)

# (d)
data = pd.merge(left = df1, right = df2, how = 'outer', on = ['Name','Duration'])
data.set_index(['Name', 'Duration'])
df6 = data.groupby(['Name', 'Duration'])
print("(d) Descriptive Statistics",df6.describe())