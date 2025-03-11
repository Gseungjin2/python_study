#초급 파이썬 변수를 사용한 데이터 관리 day1

print("Hello" + "World!")

print("Hello" + " " + "World!")

print("Hello" * 3)

print("Hello" + " World!" * 3)

print("Hello world!\nHello world!\nHello world!")

print("what is your name?")

input("what is your name?")

print("Hello " + input("What is your name?") + "!")

name = "jack" #input("What is your name?")
print(len(name))

print(len(input("What is your name?")))

username = input("What is your name?")
length = len(username)
print(length)

# 변수 이름 규칙
# 1. 변수 이름은 영어로 작성
# 2. 띄어쓰기 대신 언더바(_) 사용
# 3. 변수 이름은 숫자로 시작할 수 없음
# 4. 특수문자는 언더바(_)만 사용 가능
# 5. 예약어 사용 불가(if, function, for, while, and, or, not, True, False, None 등)


#변수 실습
glass1 = "milk"
glass2 = "juice"
 
temp = glass1
glass1 = glass2
glass2 = temp

# 만약 두 개의 실제 유리잔이 있고 우리가 내용물을 교환하려면 추가로 한 잔이 필요할 것입니다! 따라서 해결책은 임시 변수를 만들어 한 잔의 내용물을 저장하는 것입니다.

# temp = glass1
# glass1의 내용을 임시 변수에 저장함으로써, 이제 glass1 변수를 사용하여 glass2의 내용을 저장할 수 있습니다.

# glass1 = glass2
# 마지막으로, 임시 변수에 있는 내용물을 glass2에 넣을 수 있습니다.

# glass2 = temp

# 실제 유리컵을 사용하여 시도해 보세요!



#변수 이름 짓기
# 변수 이름 짓기 규칙
# 1. 변수 이름은 영어로 작성
# 2. 띄어쓰기 대신 언더바(_) 사용
# 3. 변수 이름은 숫자로 시작할 수 없음
# 4. 특수문자는 언더바(_)만 사용 가능
# 5. 예약어 사용 불가(if, function, for, while, and, or, not, True, False, None 등)
user_name = "Angela"
length = len(user_name)
print(length)


# 마지막 간단한 프로젝트
# 밴드 네임 생성기
print("Welcome to the Band Name Generator.")
city = input("what's the name of the city you grew up in?\n")
pet = input("what's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
