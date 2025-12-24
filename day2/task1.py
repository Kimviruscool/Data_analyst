# urllib : URL작업을 위한 여러 모듈을 모은 패키지

#[1] urllib.request
    # 1. urllib.request.Request(URL) : 지정한 URL에 대한 요청 객체 반환
    # 2. urllib.request.urlopen(요청객체) : 지정한 요청 객체를 실행하고 응답 객체를 반환
        # 2-1 응답객체.getcode() : 응답상태반환(2xx : 성공 , 4xx : 실패 , 5xx : 실패)
        # 2-2 응답객체.read() : 응답내용모두읽어오기 # .decode('utf-8') : HTML형식과 한글 형식 지원

import urllib.request # request 호출
url = "https://www.example.com" # 2. 요청을 보낼 url 주소를 가지는 변수
request = urllib.request.Request(url) #3. Request 객체 생성 #지정한 URL에 대한 요청을 생성
response = urllib.request.urlopen(request) #4. urlopen 메소드를 이용한 url에 대한 요청을 실행하고 응답을 반환 함수
print(response) #<http.client.HTTPResponse object at 0x0000017FD1CFBFD0>
print(response.getcode()) #200
print(response.read()) #b'<!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.<p><a href="https://iana.org/domains/example">Learn more</a></div></body></html>\n'
print(response.read().decode('utf-8'))