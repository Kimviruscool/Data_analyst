from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

def CoffeeBean(result):
    URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()

    for i in range(1,500):
        wd.get(URL)
        time.sleep(1)
        try :
            wd.execute_script("storePop2(%d)"%i)
            time.sleep(1)
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')

            store_name = []
            store_address = []
            store_tel = []

            store_name_span = soupCB.select("div.store_txt > p.name > span ")
            for a in store_name_span:
                span = a.contents[0].strip()
                store_name.append(span)

            store_address_span = soupCB.select("p.address > span ")
            for b in store_address_span:
                span = b.getText().strip()
                store_address.append(span)

            store_tel_p = soupCB.select("p.tel > a ")
            for c in store_tel_p:
                p = c.getText().strip()
                store_tel.append(p)

            result.append([store_name, store_address, store_tel])
        except Exception as e:
            print(e)
            continue

def main():
    result = []
    print("CoffeeBean store crawling >>>>>>>>>>>>>>>>>")
    CoffeeBean(result)

    CB_tbl = pd.DataFrame(result, columns=('Store','Address','Tel'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
    main()
