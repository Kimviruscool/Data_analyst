import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

from day10.Task1 import Y_predict, X_test

b_cancer = load_breast_cancer()
# print(b_cancer)

b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)

b_cancer_df['diagnosis'] = b_cancer.target
# b_cancer_df.head()

# print("유방암 진단 데이터셋 크기 : ", b_cancer_df.shape)

# print(b_cancer_df.info())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)
print(b_cancer.data[0])


print(b_cancer_scaled[0])

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

Y = b_cancer_df['diagnosis']
X = b_cancer_scaled

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

lr_b_cancer = LogisticRegression()

lr_b_cancer.fit(x_train, y_train)

Y_predict = lr_b_cancer.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

print(confusion_matrix(y_test, Y_predict))

accuracy = accuracy_score(y_test, Y_predict)
precision = precision_score(y_test, Y_predict)
recall = recall_score(y_test, Y_predict)
f1 = f1_score(y_test, Y_predict)
roc_auc = roc_auc_score(y_test, Y_predict)
print('정확도:{0.3f},정밀도:{1:3f},재현율:{2:3f},F1:{3:3f}'.format(accuracy, precision, recall, f1))

print('ROC_AUC:{0:3f}'.format(roc_auc))