### 2.1 숫자 자료형
## 소괄호에 값 그대로 대입

# print(5) 
# print(-10)
# print(3.14)
# print(1000)

# print(5+3)
# print(2*8)
# print(6/3)
# print(3 * ( 3 + 1))

# 1분 퀴즈 다음 중 숫자 자료형 -10을 출력하기 위한 방법으로 알맞은 것은?
# 1. print(- + 10) 2. print(-10) 3. print("-10") 4. print(10-)
# print(-10)

### 2.2 문자열 자료형
## 작은 따옴표('') 또는 큰 따옴표("") 사용
# print('풍선')
# print("나비")
# print("abcdefg")
# print("10")
# print("파이썬" * 3)

# ## 무조건 같은 따옴표를 사용

# # print('I don't want to go school.)
# print("I don't want to go to school")

# # 1분 퀴즈 다음 중 문자열 자료형을 표시하는 방법으로 알맞은 것은?
# # 1. 마우스 2. '마우스" 3. "마우스' 4. "마우스"
# print("마우스")

### 2.3 불 자료형
## 참과 거짓 판단
# print(5 > 10) #False
# print(5 < 10) #True

# print(True) #True
# print(False) #False

# print(not True) #False
# print(not False) #True

# print(not (5 > 10))
# print(not (5 < 10))

### 2.4 변수
## 변수란, 어떤 값을 저장하는 공간
## 대입 연산자('=')를 사용하여 변수에 값을 대입함 -> 변수를 "정의" 한다.

# name = "연탄이" #해당 변수에 값을 "해피"로 바꿔주기
# animal = "개" #해당 변수에 값을 "고양이로 바꿔주기
# age = 4
# hobby = "산책" #해당 변수에 값을 "낮잠"으로 바꿔주기
# is_male = True

# print("반려동물을 소개해 주세용")
# print("우리 집 반려 동물은 " + animal + "인데, 이름이 " + name + "예요.")
# print("연탄이는 4살이고, 산책을 아주 좋아해용. ")
# #print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해용.") #'+'로 연결할 때는 자료형이 같아야 함, 현재는 문자열과 숫자인 age를 연결하여 오류 메세지 노출
# print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해용.") #따라서 문자열과 맞춰주기 위해 숫자형 age를 str으로 감싸기, str()은 값의 자료형을 문자열로 바꿔주는 기능

# print(name, "는", age, "살이고," , hobby, "을 아주 좋아해용.") #쉼표 사용 시 -> 형변환 필요X, 값과 값 사이에 빈칸을 포함

## 형변환하기
## 문자열로 변경 str()/ 정수형으로 변경 int() -> 무조건 숫자로 된 문자열에만 사용가능/ 실수형을 변경 float() -> 무조건 숫자로 된 문자열에만 사용가능

# print(int("3"))
# # print(int("3") + "입니다.") #타입 오류 발생
# print(int(3.5)) #3 출력 소수점 이하를 버림
# # print(int("삼")) #타입 오류 발생
# print(float("3.5"))
# # print(float("삼점오")) #타입 오류 발생
# print(str(3) + "입니다.")
# print(str(3.5) + "입니다.")

# #type() 데이터의 자료형을 확인할 때 사용
# print(type(3))
# print(type("3"))
# print(type(3.5))
# print(type(str(3)))

# ## 변수는 사용하기 전에 정의해야 함
# # animal = "개"
# # age = 4
# # hobby = "산책"

# # print("반려동물을 소개해 주세용")
# # print("우리 집 반려 동물은 " + animal + "인데, 이름이 " + name + "예요.") #name을 나중에 정의함
# # name = "연탄이"
# # print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해용.")

# ## 변수는 사용하기 전에 마지막으로 저장한 값을 사용함
# name = "연탄이"
# animal = "개"
# age = 4
# hobby = "산책"

# print("반려동물을 소개해 주세용")
# print("우리 집 반려 동물은 " + animal + "인데, 이름이 " + name + "예요.") #name을 나중에 정의함
# hobby = "수영"
# print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해용.")

# number =3
# print(number)

# print("파이썬은")
# # print("처음에는")
# print("쉬워요")

### 2.6 실습 문제: 역 이름 출력하기
## 문제: 변수를 사용해 다음 문장을 출력하세용.
## 조건 1. 변수명은 station으로 한다. 2. 값은 변수에 '사당, 신도림, 인천공항' 순으로 저장한다. 3. 실행결과는 다음과 같은 형태로 나와야 한다.

# 변수에 "사당"을 넣었을 때
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

# # 변수에 "신도림"을 넣었을 때
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")

# # 변수에 "인천공항"을 넣었을 때
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

### 셀프체크
## 문제: 변수를 사용해 택배의 배송 상태를 안내하는 프로그램을 작성하세용.
## 조건 1. 변수명은 status로 한다. 2. 값은 변수에 '상품 준비, 배송 중, 배송 완료'순으로 저장한다. 3. 실행결과는 다음과 같은 형태로 나와야 한다.

# 변수에 "상품 준비"를 넣었을 때
# status = "상품 준비"
# print("주문상태 : " + status)
# status = "배송 중"
# print("주문상태 : " + status)
# status = "배송 완료"
# print("주문상태 : " + status)

# station = "사당"
# station = "신도림"
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# status = "상품준비"
# status = "배송 중"
# # status = "배송 완료"
# print(status)

## 3/15일 복습 완료