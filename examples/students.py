#!/usr/bin/env python

import pandas            as pd
import matplotlib.pyplot as plt
import seaborn           as sns

from sklearn.decomposition import PCA

sns.set()

df = pd.read_csv('../data/students.csv')
df['GradeID'] = df['GradeID'].apply(lambda x: int(x[-2:]))
df = pd.get_dummies(df)

absent_students  = df['StudentAbsenceDays_Above-7'] == 1
present_students = df['StudentAbsenceDays_Above-7'] == 0

plt.hist(df[absent_students]['GradeID'], color = 'red', alpha = 0.3)
plt.hist(df[present_students]['GradeID'], color = 'blue', alpha = 0.3)
# plt.scatter()
plt.show()
