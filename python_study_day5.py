# # 39. 파이썬 리스트로 for 반복문 사용하기
# '''
# For Loop

# for item in list_of_items:
# # Do something to each item

# 전 강의에서 배운 리스트와 반복문 이용하기
# '''
# # 예제
# # fruits = ["Apple", "Peach", "Pear"]
# # for fruit in fruits:
# #     print(fruit)
# #     print(fruit + " pie")
# #     print(fruits) # 리스트를 출력하고 싶다면 fruit 말고 ftuits print하면 리스트 자체를 출력한다
# # print(fruits) # 이런씩으로 들여쓰기를 하지 않으면 리스트를 한번만 출력한다.
# # # 실행 하면 0 ~ 2 까지 각각 순회 하여 값을 출력함

# '''
# 루프는 동일한 코드르 여러번 실행 할 수 있게 하는게 가장큰 강점이다.
# ** for 반복문은 단일 문장 실행에만 국한되지 않는다.(중요)
# 문자 블록 전체를 여러 번 실행할 수 있다.
# 인사이드 아웃사이드 들여쓰기 매우 중요하다** 
# '''

# # 40. 높은 점수 (간단한 미션)
# '''
# 파이썬은 숫자 처리에 매우 친화적인 언어이다 다른 언어에 비해서 왜냐하면 숫자 작업을 도와주는 내장 함수가 많다.
# '''

# student_scores = [150, 142, 185, 120, 184, 149, 24, 59, 68, 199, 78, 65, 89, 556]

# total_exam_score = sum(student_scores)
# # print(total_exam_score)

# sum = 0
# # 합산한 값을 저장하려면 변수가 필요하다 그래서 sum 이라는 변수를 하나 만들어준다.
# for score in student_scores:
#     sum += score

# print(sum)

# # max 를 이용해서 위에와 같이 코딩해 최대 값을 출력하라

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
        
# print(max_score)

# # for 반복문과 range() 함수

# # Range 함수는 특정 범위의 숫자를 생성해서 루프를 돌리고 싶을때 유용한 함수이다.
# # 예제 구문

# for number in range(a, b):
#     print(number)

# # 리스트를 돌리는 대신 범위를 생성하여 루프가 어떻게 작동 할지 정의 합니다.
# # range 함수 그 자체로는 아무것도 하지 않는다는 것을 기억 하는 것이 중요하다.

# print(range(1, 10)) # 이런씩의 사용은 잘못 되었다. 어떠한 값도 나오지 않고 그냥 range(1, 10) 이 출력 된다. 꼭 for 문과 사용해야한다.

# for number in range(1, 10):
#     print(number)

# '''
# 위 함수를 출력하면 1~9 가 나오고 10은 나오지 않는다. 모든 숫자 출력을 원한다면 1, 11을 입력 해줘야한다.
# 기본적으로 range 함수는 모든 수자를 하나씩 증가 시키며 진행한다.
# 다른 숫자로 증가 시키고 싶다면 끝에 쉬표를 추가하고 스텝 크기를 지정해야 한다. 3으로 지정한다면 3 씩 증가하면서 숫자가 출력된다.
# '''

# # 내가 쓴다다
# for number in range(1, 101, +1):
#     print(number)

# # 강의 영상 답

total = 0
for number in range(1, 101):
    total += number

print(total)


# 강의 영상 미니 프로젝트(FizzBuzz)
#내가 만든 코드 
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)