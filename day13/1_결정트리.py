import numpy as np
import pandas as pd

feature_name_df = pd.read_csv('UCI_HAR_Dataset/features.txt',sep='\s+',header=None,names=['index','feature_name'], engine='python')

print(feature_name_df.head())

feature_name = feature_name_df.iloc[:,1].values.tolist()
print(feature_name[:5])

x_train = pd.read_csv('UCI_HAR_Dataset/train/X_train.txt', sep='\s+', header=None, encoding='latin-1')
x_train.columns = feature_name

x_test = pd.read_csv('UCI_HAR_Dataset/test/X_test.txt', sep='\s+', header=None, encoding='latin-1')
x_test.columns = feature_name

y_train = pd.read_csv('UCI_HAR_Dataset/train/y_train.txt', sep='\s+',header=None,names=['action'], engine='python')
y_test = pd.read_csv('UCI_HAR_Dataset/test/y_test.txt', sep='\s+',header=None,names=['action'], engine='python')

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

print(x_train.head())

label_name_df = pd.read_csv('UCI_HAR_Dataset/activity_labels.txt', sep='\s+', header=None, names=['index','label'], engine='python')
label_name = label_name_df.iloc[:,1].values.tolist()

print(label_name)

from sklearn.tree import DecisionTreeClassifier

dt_HAR = DecisionTreeClassifier(random_state=156)
dt_HAR.fit(x_train, y_train)

y_predict = dt_HAR.predict(x_test)

