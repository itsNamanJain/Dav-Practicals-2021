import  pandas as pd
df = pd.DataFrame.from_dict(
    {
        'Name': ['Mudit Chauhan ', 'Seema Chopra', 'Rani Gupta', 'Aditya Narayan', 'Sanjeev Sahni','Prakash Kumar','Ritu Agarwal','Akshay Goel','Meeta Kulkarni','Preeti Ahuja','Sunil Das Gupta','Sonali Sapre','Rashmi Talwar',' Ashish Dubey','Kiran Sharma','Sameer Bansal'],
        'Birth_Month': ['December', 'January', 'March', 'October', 'February', 'December', 'September', 'August', 'July', 'November', 'April', 'January', 'June', 'May', 'February','October'],
        'Gender': ['M','F','F','M','M','M','F','M','F','F','M','F','F','M','F','M'],
        'Pass_Division': ['III','II','I','I','II','III','I','I','II','II','III','I','III','II','II','I']
    }
)
print("DataFrame: \n",df)

# (a)

dummy_gender = pd.get_dummies(df['Gender'])
dummy_division = pd.get_dummies(df['Pass_Division'])

df1 = pd.merge(
    left=df,
    right=dummy_division,
    left_index=True,
    right_index=True,
)
df2 = pd.merge(
    left=df,
    right=dummy_gender,
    left_index=True,
    right_index=True,
)
print("(a) Applying hot encoding on columns Gender and Pass_Division : \n",df2)

# (b)

df['Birth_Month'] = pd.Categorical(df['Birth_Month'],categories=['December','November','October','September','August','July','June','May','April','March','February','January'],ordered=True)
df = df.sort_values('Birth_Month',ascending=False)
print("(b) Sorting dataframe on Birth_Month :\n",df)