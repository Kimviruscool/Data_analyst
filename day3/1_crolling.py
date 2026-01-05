from bs4 import BeautifulSoup

html =  '<h1>테스트용 페이지</h1><div class="top"><ul class="menu"><li><a class="login" href="http://www.hanit.co.kr/memver/login.html"> 로그인 </a></li></ul><ul class="brand"><li><a href="www.hanbit.co.kr/media/"> 한빛미디어 </a></li><li><a href="www.hanbit.co.kr/arademy/">한빛아카데미</a></li></ul></div>'
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
print(soup.h1)

# 크롤링 허용 여부 확인하기 #robots.txt
"https://www.habit.co.kr/#robots.txt"