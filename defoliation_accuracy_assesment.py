import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
data = pd.read_csv('defoliation_verificaiton.csv')

column_name = 'test'
data[column_name] = data[column_name].replace(1, 0)
data[column_name] = data[column_name].replace(2, 1)

true_labels = data['test']
predicted_labels = data['grid_code']
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy}")
confusion_mat = confusion_matrix(true_labels, predicted_labels)
print("Confusion Matrix:")
print(confusion_mat)
classification_rep = classification_report(true_labels, predicted_labels)
print("Classification Report:")
print(classification_rep)


data = pd.read_csv('defoliation_verificaiton.csv')

# Specify the column name for checking the value
column_name = 'test'
value_to_drop = 1

# Get the index of rows to drop
rows_to_drop = data[data[column_name] == value_to_drop].index

# Drop the rows using the index
data = data.drop(rows_to_drop)

data[column_name] = data[column_name].replace(2, 1)

# Print the updated DataFrame
print(data)

true_labels = data['test']
predicted_labels = data['grid_code']
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy}")
confusion_mat = confusion_matrix(true_labels, predicted_labels)
print("Confusion Matrix:")
print(confusion_mat)
classification_rep = classification_report(true_labels, predicted_labels)
print("Classification Report:")
print(classification_rep)