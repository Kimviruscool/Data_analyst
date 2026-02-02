import numpy as np
import pandas as pd
data_df = pd.read_csv('auto_mpg.csv', header = 0, engine = 'python')

print(data_df.head())
# print(data_df.shape)

data_df = data_df.drop(['car_name','origin','horsepower'], axis=1, inplace=False)
print(data_df.head())

print(data_df.info())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

Y = data_df['mpg']
X = data_df.drop('mpg', axis=1, inplace=False)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

lr = LinearRegression()

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(mse, rmse)
print(r2_score(y_test, y_pred))

print(np.round(lr.intercept_, 2))
print(np.round(lr.coef_, 2))

coef = pd.Series(data = np.round(lr.coef_, 2), index = X.columns)
coef.sort_values(ascending=False)

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize=(16,16), ncols = 3 ,nrows = 2)
x_features = ['model_year','acceleration','displacement','weight','cylinders']
plot_color = ['r','b','y','g','r']
for i, feature in enumerate(x_features):
    row = int(i/3)
    col = i%3
    sns.regplot(x=feature, y='mpg',data=data_df, ax=axs[row,col], color=plot_color[i])

