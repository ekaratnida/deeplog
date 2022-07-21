#Todo
import pandas as pd

# 1. Load pvm (Prem virtual machine) structured data
df = pd.read_csv(r"example\data\pvm\train_data.log_structured.csv")
#print(df.head())

# 2. Use only four columns including Date, Time, EventID, ParameterList
# Don't know yet whether the EventID will be the same for new comming data !!!!.
# If not should create own encode EventID for each EventTemplate.
df = df[["Date","Time","EventId","ParameterList"]]
print(df.shape)
#print(df.head())

# 3. Create a matrix
#iterative way
max = -9999
for i in range(df.shape[0]):
    l = len(df['ParameterList'][i])
    if l > max:
        max = l
print(max)

#shortcut way
print(df["ParameterList"].str.len().max())

#for i in range(len(df['ParameterList'][0])):
ret = df['ParameterList'][0].split(',')
print(len(ret))
for i in ret:
    print(i)

# 3. Use one hot encoder to create a matrix
# rated_dummies = pd.get_dummies(df.ParameterList,prefix="Param_")
# print(rated_dummies.head())
# df = pd.concat([df, rated_dummies], axis=1)
# print(df.head())

# 4. Group by EventID (for each unique EventID)
# df = df.groupby("EventId")
# firstGroup = df.get_group((list(df.groups)[0]))
# print(firstGroup.iloc[0,0:6])
# res = firstGroup[firstGroup!=0].stack()
# print(res)
# cols = firstGroup.columns
# print(cols)
# bt = df.apply(lambda x: x > 0)
# print(bt)
# ret = bt.apply(lambda x: list(cols[x.values]), axis=1)
# print(ret)
# print(firstGroup.iloc[0,3])
# import numpy as np
# print(firstGroup.apply(np.flatnonzero))

# 5. Build one LSTM model for one EventID.

# If the error between a prediction and an observed value vector is within
# a high-level of confidence interval of the above gaussian distribution, the param value vector of 
# incoming log entry is considered normal, otherwise abnormal.