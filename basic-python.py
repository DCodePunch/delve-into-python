
TN = 200
TP = 50
FN = 40
FP = 60

#print(TN)

Sensitivity = TP / (TP + FN)
Specificity = TN / (TN + FP)

BalancedAccuracy = (Sensitivity + Specificity)/2
print(BalancedAccuracy)