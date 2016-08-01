import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../LoanStats3a.csv')
index = ['< 1 year', '1 year', '2 years', '3 years', '4 years', 
'5 years', '6 years', '7 years', '8 years', '9 years','10 years','10+ years']

mapping = pd.Series([0,1,2,3,4,5,6,7,8,9,10,11], index)
data['emp_length_int'] = data['emp_length'].map(mapping)
test_emp_len_int = data['emp_length_int']

x = test_emp_len_int
y = data['loan_amnt']
plt.xticks(x, index)

plt.hist(test_emp_len_int.dropna(), color='blue')
plt.autoscale(tight=True)
plt.xticks(rotation=45)

axes = plt.gca()
axes.set_ylim([min(y),max(y)])
axes.set_xticks([i for i in range(1,12) ])
axes.set_xticklabels(index)

plt.show()

#fig = plt.gcf()
#fig.set_size_inches(10, 10, forward=True)
#fig.savefig('test.png', dpi=100)
