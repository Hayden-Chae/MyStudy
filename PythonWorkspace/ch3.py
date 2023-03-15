## 3.1 연산자의 종류
## 3.1.1 산술 연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2 ** 3)
# print(10%3)
# print(10//3)

## 3.1.2 비교 연산자

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)

# print(3 == 3)
# print(4 == 2)
# print(3 + 4 ==7)
# print(1 != 3)

## 3.1.3 논리 연산자

# print((3>0) and (3>5))
# print((3>0) or (3>5))
# print(not(1 != 3))

## 1분 퀴즈
# print(5+3) # 8
# print(6/3) # 2.0
# print(5%3) # 2
# print((5 < 3) or (7<3)) #False

## 3.2 연산자의 우선순위

# 나중에 필요할 때 찾아봐라

## 1분 퀴즈
# print(2+3*4) 3*4 먼저 한 다음 2를 더해준다

## 3.3 변수로 연산하기

# number = 2+3*4
# print(number)
# number = number + 2 # (2+3*4) + 2
# print(number)

# += -= *= /= **= //= %=
# number = 2+3+5
# number %= 10
# print(number)

## 1분 퀴즈
# num =3
# num *=2 #6
# print(num)

## 3.4 함수로 연산하기
## 3.4.1 숫자 처리 함수

# abs(x) x의 절대값
# pow(x,y) x를 y만큼 거듭제곱
# max() 가장 큰 값
# min() 가장 작은 값
# round(x, d) x를 반올림한 값, d는 표시할 소수점 이하의 자릿수로 d가 없으면 소수점 이하 첫째 자리에서 반올림한 정수

# print(abs(-3))
# print(pow(3,5))
# print(max(3,8,5,2))
# print(min(5,3,2,4))
# print(round(3.674,1))

## 3.4.2 math 모듈

# floor() 내림
# ceil() 올림
# sqrt() 제곱근

# from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미
# # from 모듈명 import 기능
# # 모듈이란, 특정한 기능을 하는 파이썬 파일을 의미 / 직접 만들거나 파이썬에 이미 생성된 모듈을 사용 가능

# result = floor(4.99)
# print(result)
# result = ceil(3.14)
# print(result)
# result = sqrt(16)
# print(result)

# import math # math 모듈의 기능을 가져다 쓰겠다는 의미
# import 모듈명
# 모듈의 기능을 가져다 쓸 때
# result = math.floor(4.99)
# result = math.ceil(3.14)
# result = math.sqrt(16)

# 3.4.3 random 모듈

# from random import *

# print(random())
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10)+1)

# from random import *

# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정됐습니다.")

# 연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보세용
# 조건 1. 섭씨 온도를 저장하기 위한 변수를 만든다.
# 조건 2. 다음 공식을 이용해 섭씨 온도를 화씨 온도로 변환하고 새로운 변수에 저장한다. 화씨 온도 = (섭씨 온도 * 9/5 ) +32
# 조건 3. 섭씨 온도와 화씨 온도를 다음과 같이 출력한다.

# from math import *
# from random import *
# cen = 10
# fan = (cen * 9/5)+32
# print("섭씨 온도 : " + str(cen))
# print("화씨 온도 : " + str(fan))

