# day2

import urllib.request
import json
import urllib.parse

def getRequestUrl(url):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-client-Id","...")
    request.add_header("X-Naver-client-Secret", "..")

    try : #예외처ㅣㄹ
        request = urllib.request.urlopen(request)
        if request.getcode() == 200 :
            return request.read().decode('utf-8')
    except Exception as e :
        print(e)
        return None

def getNaverSearch(node, srcText, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f'/{node}.json'

    srcText = urllib.parse.quote(srcText)

    parameters = f'?query={srcText}&start={page_start}&display={display}'
    url = base + node + parameters
    print(url)

    responseDecode = getRequestUrl(url) #응답 객체 받기

    if responseDecode == None : return None #응답 객체가 없으면 None
    else : return json.loads(responseDecode) #응답객체가 있으면 JSON형식으로 반환

def getPostData(post, jsonResult, cnt):
    #응답받은 객체의 요소들
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    dic = {'cnt':cnt,'title':title,'description':description,'org_link':org_link,'link':link}
    jsonResult.append(dic)

def main() :
    node = 'news' #크롤링할 대상
    srcText = input('검색어 입력하세요.:') #2. 사용자 입력으로 받은 검색어
    cnt = 0 #3. 검색 결과 개수
    jsonResult = [] #4. 검색결과를 정리하여 저장한 리스트 변수

    #5. 네이버 뉴스 검색결과를 저장하는 객체 [code2]
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    if jsonResponse is None:
        print("점검필요")
        return None

    total = jsonResponse['total'] #6. 전체 검색 결과 개수

    while( (jsonResponse != None) and (jsonResponse['display'] != 0 ) ) :
        # 8.
        for post in jsonResponse['items'] :
            cnt += 1
            #9. [code3]
            getPostData(post, jsonResult, cnt)
        #
        start = jsonResponse['start'] + jsonResponse['display']

        if start > 1000:
            break

        jsonResponse = getNaverSearch(node, srcText, start, 100)
        
    print(f'전체검색 : {total}건')
    print(f'가져온 데이터 {cnt}건')

if __name__ == '__main__' :
    main()