import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../LoanStats3a.csv')
df_raw = data[['annual_inc', 'loan_amnt', 'grade' ]]
#select data where annual_inc is less than $500,000 since majority of loans are
#administered to this group

df = df_raw[df_raw.annual_inc<500000]
plt.hist(df.annual_inc,bins=20)
#
axes = plt.gca()
axes.set_xlim([0,200000])
axes.set_ylim([0,14500])
plt.xlabel("Income Bracket")
plt.ylabel("# of Loans")
plt.title("Frequency of Loans Based on Income Bracket")

fig = plt.gcf()
fig.set_size_inches(10, 10, forward=True)
fig.savefig('loansfreq.png', dpi=100)

plt.show()


#More to explore:
#What is the total open credit lines on these users?
#Can we map the types of jobs these people have or find a common purpose?
#What is the average interest rate? 
#histogram on the interest rate for these individauls?

#What is the distribution of loan grades for this subset of users?
index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
df_grade = df['grade']
mapping = pd.Series([0,1,2,3,4,5,6], index)
df_grade_int = df_grade.map(mapping)
df_grade_mapping = pd.DataFrame({'grade' :df_grade,
                              'grade_int': df_grade_int})
plt.hist(df_grade_int,bins=7)
axes = plt.gca()
axes.set_xticks([i for i in range(0,7) ])
axes.set_xticklabels(index)  
plt.xlabel("Grade")
plt.ylabel("# of Loans")
plt.title("No. of Loans by Grade")

fig = plt.gcf()
fig.set_size_inches(7, 7, forward=True)
fig.savefig('gradeloans.png', dpi=100)
plt.show()

