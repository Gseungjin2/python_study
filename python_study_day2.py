# 파이썬의 기본 데이터 형식
print(len("Hello"))

#subscript
print("Hello"[4]) 
# 문자열에서 특정 요소를 추출하는 이 방법을 서브스크립트(subscript)라고 한다. 
# 음수(-1)를 사용하여 마지막 문자를 가지고 올수도 있다.

#srting
print("123" + "456") 
# srting 방식은 숫자를 더하는게 아니라 text(문자)로 인식 하기때문에 실행시 "123456"으로 나온다

# Integer = whole number
print(123 + 456)
print(123_456_789)
# 미국에서는 천단위부터 , 를 붙이는걸 선호하고 이걸 컴퓨터에서는 _ 를 사용한다(컴퓨터에서는 int(숫자)타입에서 _를 인식 하지않음)

# Float = Floatting Point Number(부동 소수점의 줄임말)
print(3.14159)
print(3141.59)
# 소수점이 숫자 주위를 떠다닐 수 있다고 생각하면 이는 어느 지점에서든 발생할 수 있기 때문에 부동 소수점이 된다.

# Boolean
print(True)
print(False)

# 형식 오류와 형식 확인, 그리고 형 변환
print(len("12345"))
print(type("Hello"))
print(type(123))
print(type(3.14159))
print(type(True))
print(int("123") + int("456"))
# print(int("abc") + int("456")) # 이런씩의 형 변환는 불가능하다.
# len 유일하게 숫자 타입을 지원하지 않는다
# type 데이터 타입을 알려주는 유용한 내장 함수
# 데이터 형 변환을 하려면 타입 변환 또는 타입 캐스팅을 해야함

# 미션
print("Number of letters in your name: " + str(len(input("Enter your name")))) #내가 쓴답

#정답
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in yout name: " + str(length_of_name))

# 파이썬의 수학 연산
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(type(6 / 3)) # 나누기인데 부동 소수점이 출력된다.. 암시적인 형 변환이란다.. #ytep = float
print(type(6 // 3)) # 이렇게 나누면 정수로 출력한다 주의 사항 그냥 소수점을 없애 버리기 때문에 5 / 3 같은 소수점이 필요한 수는 조심해야한다. # ytpe = int
print(2 ** 3) # 거듭제곱이다
#주의 사항 동의한 코드에 여러게의 연산이 있을경우 연산 순서가 존재 나눗셈, 곱셈 최우선 그 다음 덧셈 뺄셈 다음 연산 순위로 간다
# PEMDAS (괄호, 지수, 나눗셈, 덧셈, 뺄셈) 순서이다
# ()
# **
# * OR / 
# + OR - 
# 곱셈, 나눗셈 == 같은 순위 이고 맨 왼쪽에있는 연산 부터 시작이다 +, -기도 같다
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#print(3 * 3 + 3 / (3 - 3)) #내가 만들 정답답 division bu zero 0으로 나눈거나 곱하려고 해서 나는 에러

# mbi 계산기
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height ** 2
# bmi = weight // height ** 2
# bmi = 84 / 1.65 ** 2

print(bmi)
print(int(bmi)) #반올림하여 가장 낮은 정수로 내림 처리
print(round(bmi)) #전통적인 수학적 의미에서 반올림을 수행하는 round 함수가 있음 ex) 0.5이상 높으면 반올림
print(round(bmi, 2)) # 이런씩으로 내가 소수점 2번째 자리까지 반올림 하고 싶은면 이런씩으로 사용가능하다.
                     # 소수점 두번째 자리까지 정확하게 반올림된 부동 소수점 숫자로 변환 된다.

score = 0

# user scores a point
score += 1
score -= 1
print(score)

# f-strings
print("Your score is" + str(score)) # 이런씩의 형 변환은 매번 하기 불편하다.

score = 0 
heigth = 1.0
is_winning = True

print(f"Your score is = {score}, your heigth is {heigth}, You are winning is {is_winning}")

# 2일차 프로젝트 : 팁 계산기 만들기

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_bill = bill * (1 + tip_percentage)
per_person = total_bill / people
final_amount = round(per_person, 2)

print(f"Each person should pay: ${final_amount}")


# 영상에서의 답안
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill =  bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")