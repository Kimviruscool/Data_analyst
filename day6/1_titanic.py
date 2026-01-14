import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")
titanic.to_csv("titanic.csv", index=False)
print(titanic.isnull().sum())
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
print(titanic['embarked'].value_counts())
print(titanic.info())

import matplotlib.pyplot as plt
f, ax = plt.subplots(1,2,figsize=(10,5))
titanic['survived'][titanic['sex']=='male'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0], shadow=True)
titanic['survived'][titanic['sex']=='female'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[1], shadow=True)
ax[0].set_title("Survived (Male)")
ax[1].set_title("Survived (Female)")
plt.show()