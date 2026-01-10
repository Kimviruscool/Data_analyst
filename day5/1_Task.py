import pandas as pd
red_df = pd.read_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-red.csv",sep=';',header=0, engine='python')
white_df = pd.read_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-white.csv",sep=';',header=0, engine='python')
red_df.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-red2.csv",index=False)
white_df.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/winequality-white2.csv",index=False)

print(red_df.head())
red_df.insert(0,column='type',value='red')
print(red_df.head())
print(red_df.shape)

print(white_df.head())
white_df.insert(0,column='type',value='white')
print(white_df.head())
print(white_df.shape)

wine = pd.concat([red_df,white_df])
print(wine.shape)

wine.to_csv("C:/Users/0000/Desktop/Data_analyst/day5/wine.csv", index=False)

print(wine.info())

wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())
print(wine.describe())
sorted(wine.quality.unique())
wine.quality.value_counts()


