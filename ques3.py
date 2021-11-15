import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(50, 4)), columns=list('ABCD'))
columns = list(df)
i = 0;
col_list = ["A", "B", "C", "D"]
while i < 20:
    r_row = np.random.randint(0, 50)
    r_col = np.random.choice(col_list)
    df.loc[r_row, r_col] = np.nan
    i = i + 1
print("Dataframe Generated : \n",df.head())

print("(a) Missing Values in dataframe in each column\n", df.isnull().sum())
print("(b) Dropping column having more than 5 null values")
mod_df = df.drop(df.columns[df.apply(lambda col: col.isnull().sum() > 5)], axis=1)
print(mod_df.head())
print("(c) Dropping with with maximum sum")
res = df.sum(axis=1).idxmax()
update_df = df.drop(res)
print(update_df.head())
print("(d) Sorting dataframe acc to first column")
sorted_df = df.sort_values(by=['A'], ascending=True)
print(sorted_df.head())
print("(e) Removing duplicates from dataframe")
rd_df = df.drop_duplicates(subset='A', keep="last")
print(rd_df.head())
print("(f) Correlation b/w first and second column and Covariance b/w second and third column")
column_1 = df["A"]
column_2 = df["B"]
column_3 = df["C"]
correlation = column_1.corr(column_2)
print("Correlation :\n", correlation)
covariance = column_2.cov(column_3)
print("Covariance : \n", covariance)
print("(g) Removing rows with outliers")
from scipy import stats

rm_out_df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
print(rm_out_df.head())
print("(h) Discretize second column and create 5 bins")
print(pd.qcut(df['B'], q=5).head())
