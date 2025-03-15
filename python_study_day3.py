# """
# # if / else 및 조건 연산자를 통한 흐름 제어
# # conditional
# # if / else 특정 조건을 따라서 A 또는 B를 수행하게 되며 파이썬 코드 예제

# # 욕조 물 높이를 이용한 조건문
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")
# """

# """
# # 물 높이가 50이라고 할때 80보다 높으면 멈추고 80 print("Drain water") 
# # 만약 80보다 작으면 else: print("Continue") 넘어가서 물을 계속 채운다
# """

# # 롤러 코스터 이용한 조건문
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# """
# # 120 이상만 탈수 있다면 > 이 연산자 만으론 120 포함이 안되기에 >= 크거나 같은 연사자를 사용하는게 좋다.
# # 연산자
# # > (Greater than) 크다(초과)
# # < (Less than) 작다(미만)
# # >= (Greater than or equal to) 크거나 같다
# # <= (Less than or equal to) 작거나 같다
# # == Equal to 동일하다 & 같다
# # != Not equal to 동일하지 않다 & 부정
# """

# """
# # Modulo 소개
# # 새로운 연산자 Modulo Operator = % 
# # (단순한 퍼센트 기호가 아니다 두숫자 사이에 위치하고 따라서 
# # 이진 연사자이며 나눈셈 후에 나머지를 게산하는 연산자이다.)
# # (ex) (10 % 5 = 0 & = 10 % 5 = 2) 나머지가 없기 때문에 깔끔하다.
# # ((ex) (10 % 3 = & 10 / 3 = 3.3333333) 인데 % 연사자를 사용하면 10 % 3 == 10 / 3 = 3 with 1 remaining 따라서
# # 10 % 3 = 1 이 된다. % 가 나머지를 알려주기 때문에
# # 
# # Even number 12 % 2 == 0 & 12 / 2 == 0
# """

# number_to_check = int(input("What is the number you want to check?"))

# # print(number_to_check % 2)

# if number_to_check % 2 == 0:
#     print("Even") # Even = 짝수
# else:
#     print("Odd") # Odd = 홀수

# # 이 함수는 홀 짝 구분 할 수있는 함수 이기도 한 것 같다..

# """
# # 중첩 if 문과 elif 문
# # Nested if / else

# # if condition:
# #     if another condition:
# #         do this
# #     else:
# #         do this
# # else:
# #     do this 
# # if문 안에 또 다른 if문과 else문을 가질 수 있다.
# # 하위 if문을 실행하기 위해서는 상위 if문이 참이어야하고 하위 if 문도 참이어야 한다.
# # else문을 실행하려면 상위 if문은 참이지만 하위 if문은 거짓이어야 한다.
# # 그래서 else 블록으로 들어가야하는지 아니면 if문 안의 중첩 블록으로 들어가야하는지가 중요하다.
# """

# # 위에서 배운 롤러코스터를 중첩 if 를 사용해서 업그레이드하기
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your ahe?"))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# # 나이의 조건이 두가지가 아니라 3가지 일 때 elif를 사용할 수 있다. (if / elif / else)

# # 미니 프로젝트 해설이 포함됨 BMI 계산기

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25: 
#     print("normal weight")  
# else:
#     print("overweight")

# # 다중 연속 if 문
# """
# # if / elif / else = A,B 또는 C 중 하나만 수행 
# # if condition1:
# #     do A
# # elif condition2:
# #     do B
# # else:
# #     do C

# # #  Multiple if = 세가지 조건을 모두 확인함 모두가 True 라면 세가지 조건 모두 실행함
# # if condition1:
# #     do A
# # if condition2:
# #     do B
# # if condition3:
# #     do C
# """

# 롤러코스터 Multiple if 사용해서 업그레이드하기

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.?")
#     if wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3
    
#     print(f"Your fianl bill is {bill}") 
#     """
#     이 print 문은 같은 간격으로 들여쓰기 X 실직적으로 if 문이 실행된 후에 발생한다. 
#     확인해보고 싶은면 print 문을 들여쓰기 해보라.
#     """
# else:
#     print("Sorry you have to grow taller before you can ride.")

# wants_photo 와 age가 같은 블록에 있지만 wants_photo 조건문이 동일한 들여쓰기 간격이 아님을 주의가 필요하다.

# 피자 주문 실습

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M ro L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y ro N: ")
bill = 0

if size == "S":
    bill = 15
    print("Pizza Small $15")
elif size == "M":
    bill = 20
    print("Pizza medium $20")
elif size == "L":
    bill = 25
    print("Large Pizza $25")
else:
    print("You typed the wrong inputs.")
    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    bill += 1
            
print(f"Your fianl bill is {bill}")

# 논리 연산자
"""
Lofical Operators 
A and B
C ro D
not E
"""