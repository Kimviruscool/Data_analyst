import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

print(housing.DESCR)

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df.head())

housing_df['PRICE'] = housing.target
print(housing_df.head())

print("캘리포니아 주택 가격 데이터셋 크기 :", housing_df.shape)
print(housing_df.info(),"\n")

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

Y = housing_df['PRICE']
X = housing_df.drop('PRICE', axis=1, inplace=False)

x_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=156)

lr = LinearRegression()

lr.fit(x_train, y_train)

Y_predict = lr.predict(X_test)

mse = mean_squared_error(y_test, Y_predict)
rmse = np.sqrt(mse)

print('MSE : {0:3f}, RMSE : {1:3f}'.format(mse, rmse))
print('R^2(Varicance score) : {0:3f}'.format(r2_score(y_test, Y_predict)))

print("Y절편 값 : ",lr.intercept_)
print("회귀 계수 값 : ", np.round(lr.coef_, 1))

coef = pd.Series(data = np.round(lr.coef_,2), index = X.columns)
print(coef.sort_values(ascending = False))

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize=(16,12), ncols=3, nrows=5)

x_features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

for i , feature in enumerate(x_features):
    row = int(i/3)
    col = i%3
    sns.regplot(x=feature, y = 'PRICE', data = housing_df, ax = axs[row,col])

if len(x_features) < 9:
    axs[2, 2].axis('off')