import pandas as pd
red_df = pd.read_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-red.csv",sep=';',header=0, engine='python')
white_df = pd.read_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-white.csv",sep=';',header=0, engine='python')
red_df.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-red2.csv",index=False)
white_df.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-white2.csv",index=False)

# print(red_df.head())
red_df.insert(0,column='type',value='red')
# print(red_df.head())
# print(red_df.shape)

# print(white_df.head())
white_df.insert(0,column='type',value='white')
# print(white_df.head())
# print(white_df.shape)

wine = pd.concat([red_df,white_df])
# print(wine.shape)

wine.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/wine.csv", index=False)

# print(wine.info())

wine.columns = wine.columns.str.replace(' ', '_')
# print(wine.head())
# print(wine.describe())
# sorted(wine.quality.unique())
wine.quality.value_counts()

#그룹 비교
wine.groupby('type')['quality'].describe()
wine.groupby('type')['quality'].mean()
wine.groupby('type')['quality'].std()
wine.groupby('type')['quality'].agg(['mean','std'])

from scipy import stats
from statsmodels.formula.api import ols, glm
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
stats.ttest_ind(red_wine_quality, white_wine_quality, equal_vars=False)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + ph + sulphates alcohol'
regression_result = ols(Rformula, data = wine).fit()
regression_result.summary()