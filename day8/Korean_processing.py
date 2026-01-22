import json
import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

inputFileName = 'etnews.kr_facebook_2016-01-01_2018-08-01_4차 산업혁명.json'
file = open(inputFileName,'r',encoding='utf-8')
filedata = file.read()
data = json.loads(filedata)
# print(data)

message = ''
for item in data:
    if 'message' in item.keys():
        message = re.sub(r'[^\w]]','',item['message'])+''

print(message)

nlp = Okt()
message_N = nlp.nouns(message)
print(message_N)

count = Counter(message_N)
print(count) # 반복 횟수 카운트

word_count = dict() #dictionary 생성
for tag,counts in count.most_common(80):
    if(len(str(tag))>1):
        word_count[tag] = counts
        print("%s : %d" % (tag,counts))

print(word_count)

font_path = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

plt.figure(figsize=(12,15))
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.grid(True)
sorted_keys = sorted(word_count, key=word_count.get, reverse=True)
sorted_values = sorted(word_count.values(), reverse=True)
plt.bar(range(len(word_count)), sorted_values, align='center')
plt.xticks(range(len(word_count)), list(sorted_keys), rotation=75)
plt.show()

wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

# cloud.to_file(inputFileName+'_Cloud.jpg')
# 워드클라우드 이미지 결과 저장