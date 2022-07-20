#Todo

# 1. Load pvm structured data

# 2. Use only four columns including Date, Time, EventID, ParameterList

# 3. Group by EventID (for each unique EventID)

# 4. Use one hot encoder to create a matrix

# 5. Build one LSTM model for one EventID.

# If the error between a prediction and an observed value vector is within
# a high-level of confidence interval of the above gaussian distribution, the param value vector of 
# incoming log entry is considered normal, otherwise abnormal.