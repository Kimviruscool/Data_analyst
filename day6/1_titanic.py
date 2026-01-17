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

sns.countplot(x='pclass', hue='survived', data=titanic)
plt.title('pclass vs Survived')
plt.show()

titanic_corr = titanic.corr(method='pearson',numeric_only=True)
print(titanic_corr)

titanic_corr.to_csv("titanic_corr.csv", index=False)

print(titanic['survived'].corr(titanic['adult_male']))
print(titanic['survived'].corr(titanic['fare']))

sns.pairplot(titanic, hue='survived')
plt.show()

def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:
        return 7

titanic['age2'] = titanic['age'].apply(category_age)
titanic['sex'] = titanic['sex'].map({'male':1, 'female':0})
titanic['family'] = titanic['sibsp']+titanic['parch']+1
titanic.to_csv("titanic3.csv", index=False)
heat_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
colormap = plt.cm.RdBu
sns.heatmap(heat_data.astype(float).corr(),linewidths=0.1, vmax=1.0, square=True, cmap=colormap,linecolor='white',annot=True,annot_kws={'size':10})
plt.show()