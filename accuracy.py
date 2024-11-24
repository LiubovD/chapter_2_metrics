
TP = 1401
FP = 1101
FN = 401

Accuracy = (TP) / (TP + FP + FN)
Precision = (TP) / (TP + FP)
Recall = (TP) / (TP + FN)
F1_Score = 2 * (Precision * Recall) / (Precision + Recall)
print("Recall=", Recall)
print("Precision=", Precision)
print("F1-Score=", F1_Score)

