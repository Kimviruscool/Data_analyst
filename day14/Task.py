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

customer_df['Freq_log'] = np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log'] = np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log'] = np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())

fig,ax = plt.subplots()
ax.boxplot([customer_df['Freq_log'],customer_df['SaleAmount_log'],customer_df['ElapsedDays_log']], sym='bo')
plt.xticks([1,2,3],['Freq_log','SaleAmount_log','ElapsedDays_log'])
plt.show()

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

X_feature = customer_df[['Freq_log','SaleAmount_log','ElapsedDays_log']].values

from sklearn.preprocessing import StandardScaler
X_feature_scaled = StandardScaler().fit_transform(X_feature)

distortions = []

for i in range(1, 11):
    kmeans_i = KMeans(n_clusters=i, random_state = 0)
    kmeans_i.fit(X_feature_scaled)
    distortions.append(kmeans_i.inertia_)

plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0)
Y_labels = kmeans.fit_predict(X_feature_scaled)

customer_df['ClusterLabel'] = Y_labels
print(customer_df.head())

from matplotlib import cm

def silhoutteViz(n_cluster, X_features):
    kmeans = KMeans(n_clusters=n_cluster, random_state=0)
    Y_labels = kmeans.fit_predict(X_features)

    silhouette_values = silhouette_score(X_features, Y_labels, metric='euclidean')

    y_ax_lower, y_ax_upper = 0,0
    y_ticks = []

    for c in range(n_cluster):
        c_silhouettes = silhouette_values[Y_labels == c]
        c_silhouettes.sort()
        y_ax_upper += len(c_silhouettes)
        color = cm.jet(float(c)/n_cluster)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouettes, height=1.0, edgecolor='none', color=color)
        y_ticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouettes)

    silhouette_avg = np.mean(silhouette_values)
    plt.axvline(x=silhouette_avg, color='k', linestyle='--')
    plt.title('Number of Cluster : '+ str(n_cluster) + '\n' + 'Silhouette Score:'+str(round(silhouette_avg,3)))
    plt.yticks(y_ticks,range(n_cluster))
    plt.xticks([0,0.2,0.4,0.6,0.8,1])
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient')
    plt.tight_layout()
    plt.show()

def clusterScatter(n_cluster, X_features):
    print('ing')