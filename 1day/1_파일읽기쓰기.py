# 1_파일읽기쓰기

# (1) 파일 생성, open(파일이름, 열기모드)
    # 해당 파일 객체를 반환 해주는 함수
    # 열기모드 : r읽기, w쓰기 a추가
    # 파일 닫기 : 파일객체변수.close
    # 파일 열기 : 파일객체변수 = open(파일이름, 열기모드)
# 1 열기
f = open('새파일.txt','w') #쓰기모드로 파일 열기
print(f)
# 2 파일닫기
f.close()

# 2 파일을 쓰기 모드로 열어 내용 쓰기
f = open("c:/users/0000/desktop/doit/새파일.txt", "w") #해당 경로의 파일을 쓰기모드로 열어서 객체 반환
# C:\Users\0000\Desktop\doit
for i in range(1, 11) : #1부터 11미만까지 반복 1~10
    data = f'{i}번째 줄입니다. \n'
    #내용 작성하기
    f.write(data)

f.close()

# 파일을 읽는 여러가지 방법
# 1. readline 첫번째 줄을 읽어오는 함수
f = open("c:/users/0000/desktop/doit/새파일.txt", 'r') # 해당 파일을 읽기모드 객체 반환
line = f.readline()
print(line)
f.close()
# 2. readlines 모든 줄을 읽어오는 함수 (요소 1개씩 읽어서 반복변수에 대입하여 반환)
f = open("c:/users/0000/desktop/doit/새파일.txt", 'r') # 해당 파일을 읽기모드 객체 반환
line = f.readlines()
print(line)
f.close()
# 3. read 모든 줄을 읽어오는 함수 (파일전체를 문자열로 읽어옴)
f = open("c:/users/0000/desktop/doit/새파일.txt", 'r') # 해당 파일을 읽기모드 객체 반환
line = f.read()
print(line)
f.close()

#4. 파일 객체와 for문

f = open("c:/users/0000/desktop/doit/새파일.txt", 'r')
for str in f:
    print(str) #파일 객체내 한줄씩 반복변수에 대입하여 반복처리
f.close()

# 파일에 새로운 내용 추가
f = open("c:/users/0000/desktop/doit/새파일.txt", 'a') #파일 추가모드
for value in range(11, 20):
    data = f'{value}번째 줄입니다 \n'
    f.write(data)
f.close()

# 확인
f = open("c:/users/0000/desktop/doit/새파일.txt", 'r')
print(f.read())

# 파일은 항상 파일을 열고 작업이 끝나면 파일을 닫는 것을 해야한다. #with 절에서 자원을 획득하고 사용하고 반납 한다.
    #with 자료생성 as 변수 :
        # 해당 자료를 변수에 대입하고 with 종료되면 자동으로 변수는 초기화
with open("foo.txt", 'w') as f :
    f.write("Life is too short, you need python")
