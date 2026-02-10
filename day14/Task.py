import pandas as pd
import math

retail_df = pd.read_excel('Online_Retail.xlsx')
# print(retail_df.head())
#
# print(retail_df.info())

retail_df = retail_df[retail_df['Quantity']>0]
retail_df = retail_df[retail_df['UnitPrice']>0]
retail_df = retail_df[retail_df['CustomerID'].notnull()]

#자료형 정수형 전환
retail_df['CustomerID'] = retail_df['CustomerID'].astype(int)

# print(retail_df.info())
# print(retail_df.isnull().sum())
# print(retail_df.shape)

retail_df.drop_duplicates(inplace=True)
print(retail_df.shape)

pd.DataFrame([{'Product':len(retail_df['StockCode'].value_counts()),
               'Transaction':len(retail_df['InvoiceNo'].value_counts()),
               'Customer':len(retail_df['CustomerID'].value_counts())}],
             columns=['Product','Transaction','Customer'], index = ['counts'])

retail_df['Country'].value_counts()

retail_df['SaleAmount']=retail_df['UnitPrice']*retail_df['Quantity']
print(retail_df.head())

aggregations = {
    'InvoiceNo' : 'count',
    'SaleAmount' : 'sum',
    'InvoiceDate' : 'max'
}

customer_df = retail_df.groupby('CustomerID').agg(aggregations)
customer_df = customer_df.reset_index()
customer_df.head()

customer_df = customer_df.rename(columns = {'InvoiceNo' : 'Freq', 'InvoiceDate':'ElapsedDays'})
# print(customer_df.head())

import datetime

customer_df['ElapsedDays'] = datetime.datetime(2011,12,10) -customer_df['ElapsedDays']

customer_df['ElapsedDays'] = customer_df['ElapsedDays'].apply(lambda x:x.days+1)

print(customer_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq'], customer_df['SaleAmount'], customer_df['ElapsedDays']], sym='bo')
plt.xticks([1,2,3],['Freq','SaleAmount','ElapsedDays'])
plt.show()

import numpy as np

