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

round(3.425, 1)