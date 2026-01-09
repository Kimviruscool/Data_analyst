#동적 웹페이지 크롤링

from selenium import webdriver

wd = webdriver.Chrome()
# wd.get("http://www.hanbit.co.kr")
# coffeebean
from bs4 import BeautifulSoup
wd.get("https://www.coffeebeankorea.com/store/store.asp")
wd.execute_script("storePop2(1)")
html = wd.page_source
soupCB1 = BeautifulSoup(html, 'html.parser')
print(soupCB1.prettify())

store_name_sapn = soupCB1.select("div.store_txt > p.name > span ")

store_name = []

for span in store_name_sapn:
    name = span.contents[0].strip()
    # print(name)
    store_name.append(name)

print(store_name)

add = []

store_address = soupCB1.select("p.address > span ")
for stores in store_address:
    address = stores.getText().strip()
    # print(address)
    add.append(address)

# store_address = store_address[0].string
print(add)

phone = []

store_num = soupCB1.select("p.tel > a ")
for num in store_num:
    nummber = num.getText().strip()
    phone.append(nummber)

print(phone)