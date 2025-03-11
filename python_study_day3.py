# if / else 및 조건 연산자를 통한 흐름 제어
# conditional
# if / else 특정 조건을 따라서 A 또는 B를 수행하게 되며 파이썬 코드 예제

# 욕조 물 높이를 이용한 조건문
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
# 물 높이가 50이라고 할때 80보다 높으면 멈추고 80 print("Drain water") 
# 만약 80보다 작으면 else: print("Continue") 넘어가서 물을 계속 채운다

# 롤러 코스터 이용한 조건문
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

# 120 이상만 탈수 있다면 > 이 연산자 만으론 120 포함이 안되기에 >= 크거나 같은 연사자를 사용하는게 좋다.
# 연산자
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)
# == Equal to
# != Not equal to

# Modulo 소개
# 새로운 연산자 Modulo Operator = % 
# (단순한 퍼센트 기호가 아니다 두숫자 사이에 위치하고 따라서 
# 이진 연사자이며 나눈셈 후에 나머지를 게산하는 연산자이다.)
# (ex) (10 % 5 = 0 & = 10 % 5 = 2) 나머지가 없기 때문에 깔끔하다.
# ((ex) (10 % 3 = & 10 / 3 = 3.3333333) 인데 % 연사자를 사용하면 10 % 3 == 10 / 3 = 3 with 1 remaining 따라서
# 10 % 3 = 1 이 된다. % 가 나머지를 알려주기 때문에
# 
# Even number 12 % 2 == 0 & 12 / 2 == 0

number_to_check = int(input("What is the number you want to check?"))

# print(number_to_check % 2)

if number_to_check % 2 == 0:
    print("Even") # Even = 짝수
else:
    print("Odd") # Odd = 홀수

# 이 함수는 홀 짝 구분 할 수있는 함수 이기도 한 것 같다..

# 중첩 if 문과 elif 문
# Nested if / else

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this 
# if문 안에 또 다른 if문과 else문을 가질 수 있다.
# 하위 if문을 실행하기 위해서는 상위 if문이 참이어야하고 하위 if 문도 참이어야 한다.
# else문을 실행하려면 상위 if문은 참이지만 하위 if문은 거짓이어야 한다.
# 그래서 else 블록으로 들어가야하는지 아니면 if문 안의 중첩 블록으로 들어가야하는지가 중요하다.

# 위에서 배운 롤러코스터를 중첩 if 를 사용해서 업그레이드하기
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your ahe?"))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# 나이의 조건이 두가지가 아니라 3가지 일 때 elif를 사용할 수 있다. (if / elif / else)