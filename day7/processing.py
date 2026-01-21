import pandas as pd
import glob
import re
from functools import reduce
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('wordnet')

all_file = glob.glob('myCabinetExcelData*.xls')
# all_file = glob.glob('day7/export*.csv')
print(all_file)

all_files_data = []
for file in all_file:
    data_frame = pd.read_excel(file)
    all_files_data.append(data_frame)

# print(all_files_data[0])

all_files_data_concat = pd.concat(all_files_data, axis=0, ignore_index=True)
# print(all_files_data_concat)

all_files_data_concat.to_csv('data.csv', encoding='utf-8', index=False)

all_title = all_files_data_concat['제목']
# print(all_title)

stopWords = set(stopwords.words('english'))
lemma = WordNetLemmatizer()
words = []

for title in all_title:
    EnWords = re.sub(r"[^a-zA-Z]+","",str(title))
    EnWordsToken = word_tokenize(EnWords.lower())
    EnWordsTokenStop = [w for w in EnWordsToken if w not in stopWords]
    EnWordsTokenStopLemma = [lemma.lemmatize(w) for w in EnWordsTokenStop]
    words.append(EnWordsTokenStopLemma)

# print(words)

words2 = list(reduce(lambda x, y: x+y, words))
# print(words2)

count = Counter(words2)
print(count)

word_count = dict()

for tag, counts in count.most_common(50):
    if(len(str(tag))>1):
        word_count[tag] = counts
        print("%s : %d" % (tag, counts))

sorted_keys = sorted(word_count, key = word_count.get, reverse = True)
sorted_Values = sorted(word_count.values(), reverse = True)
plt.bar(range(len(word_count)), sorted_Values,align='center')
plt.xticks(range(len(word_count)), list(sorted_keys), rotation=85)
plt.show()

if 'big' in word_count:
    del word_count['big']

if 'data' in word_count:
    del word_count['data']

all_files_data_concat['doc_count'] = 0
summary_year = all_files_data_concat.groupby('출판일', as_index=False)['doc_count'].count()
print(summary_year)

plt.figure(figsize = (12,5))
plt.xlabel("year")
plt.ylabel("doc-count")
plt.grid(True)
plt.plot(range(len(summary_year)), summary_year['doc_count'])
plt.xticks(range(len(summary_year)), [text for text in summary_year['출판일']])
plt.show()

stopwords = set(STOPWORDS)
wc = WordCloud(background_color='ivory', stopwords=stopwords, width = 800, height = 600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize = (8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

cloud.to_file('myCabinetExcelData.jpg')