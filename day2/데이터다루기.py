#73회차 데이터다루기 클래스1

#함수 정의
def nameCreate() :
    return

def nameRead() :
    return

def nameUpdate() :
    return

def nameDelete() :
    return

#전역 변수
names = "BEE,Lee,Yoon"

while True : #무한루프 #{} 대신 : 과 들여쓰기를 사용 # true 소문자가 아닌 True 대문자로 작성
    ch = int( input() )
    # input() 입력함수 , 받은 데이터를 문자열 반환
    # #int 문자열타입 > 정수타입 변환
    # ch : 'ch' 변수에 특정한 타입을 작성/명시 하지는 않는다.
    if ch == 1 : #조건문 #만약에
        # 주의할점 : 들여쓰기
        nameCreate()
    elif ch == 2 : nameRead() #함수 호출
    elif ch == 3 : nameUpdate()
    elif ch == 4 : nameDelete()