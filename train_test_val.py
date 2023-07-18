import random
import pandas as pd
import pickle

output_folder='csv_files/'
dataset_folder='ISDT_dummies/'
db_data = pd.read_csv(output_folder+'ISDT_dataset_new - Copy.csv')
print(db_data.columns) 

X=db_data
X=db_data.drop(['FINAL Submission Area  [Total Pts: 100 Score] |531746'],axis=1)
for col in X.columns:
       print(X[col].dtypes)
       if(X[col].dtypes!='float64'):
              X[col] = X[col].astype('category')
              X[col] = X[col].cat.codes 
print(X)
y=db_data['FINAL Submission Area  [Total Pts: 100 Score] |531746'] 
result = pd.concat([X, y], axis=1)

for col in result.columns:
    print(result[col].dtypes)
    result[col] = result[col].astype('float64') 
result
print(result) 
result=result
result.to_csv(output_folder+'ISDT_dummies_data.csv',header=False, index=False)


# Set the proportion of data for each split
train_ratio = 0.7  # 70% for training
val_ratio = 0.15   # 15% for validation
test_ratio = 0.15  # 15% for testing

# Get the total number of samples
total_samples = len(result)

# Shuffle the data indices
indices = list(range(total_samples))
random.shuffle(indices)

# Calculate the number of samples for each split
train_size = int(total_samples * train_ratio)
val_size = int(total_samples * val_ratio)

# Split the data based on the calculated sizes and shuffled indices
train_indices = indices[:train_size]
val_indices = indices[train_size:train_size+val_size]
test_indices = indices[train_size+val_size:]

# Split the features and labels into train, validation, and test sets
result_train = result.iloc[train_indices]
# y_train = y.iloc[train_indices]

result_val = result.iloc[val_indices]
# y_val = y.iloc[val_indices]

result_test = result.iloc[test_indices]
# y_test = y.iloc[test_indices]

# # Print the lengths of the resulting datasets
# print("Training data length:", len(X_train), len(y_train))
# print("Validation data length:", len(X_val), len(y_val))
# print("Test data length:", len(X_test), len(y_test))
# Print the lengths of the resulting datasets
print("Training data length:", len(result_train))
print("Validation data length:", len(result_val))
print("Test data length:", len(result_test))
 
result_train.to_csv(dataset_folder+'train/train.dat',sep=',', header=False,index=False)
result_test.to_csv(dataset_folder+'test/test.dat',sep=',', header=False,index=False)
result_val.to_csv(dataset_folder+'val/val.dat',sep=',', header=False,index=False)
 

