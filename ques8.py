import  pandas as pd
df = pd.DataFrame.from_dict(
    {
        'Name': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats','Kumar','Shah','Shah','Kumar','Vats'],
        'Gender': ['Male','Male','Female','Female','Female','Male','Male','Female','Female','Male',],
        'Monthly_Income (Rs.)': [114000.00,65000.00,43150.00,69500.00,155000.00,103000.00,55000.00,112400.00,81030.00,71900.00]
    }
)
print("Dataframe : \n",df)

# (a)
df1 = df.groupby('Name').sum()
print("(a) Family-wise gross monthly income :\n",df1)

# (b)
df2 = df.groupby('Name').max()
print("(b) Member with the highest monthly income in a family : \n",df2)

# (c)
df3 = df[df['Monthly_Income (Rs.)']>60000.00]
print("(c) Monthly income of all members with income greater than Rs. 60000.00 :\n",df3)

# (d)
df4 = df[(df["Name"]=="Shah")&(df["Gender"]=="Female")]
print("(d) Average monthly income of the female members in the Shah family : \n",df4["Monthly_Income (Rs.)"].mean())