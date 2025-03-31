# 39. 파이썬 리스트로 for 반복문 사용하기
'''
For Loop

for item in list_of_items:
# Do something to each item

전 강의에서 배운 리스트와 반복문 이용하기
'''
# 예제
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits) # 리스트를 출력하고 싶다면 fruit 말고 ftuits print하면 리스트 자체를 출력한다
# print(fruits) # 이런씩으로 들여쓰기를 하지 않으면 리스트를 한번만 출력한다.
# # 실행 하면 0 ~ 2 까지 각각 순회 하여 값을 출력함

'''
루프는 동일한 코드르 여러번 실행 할 수 있게 하는게 가장큰 강점이다.
** for 반복문은 단일 문장 실행에만 국한되지 않는다.(중요)
문자 블록 전체를 여러 번 실행할 수 있다.
인사이드 아웃사이드 들여쓰기 매우 중요하다** 
'''

# 40. 높은 점수 (간단한 미션)
'''
파이썬은 숫자 처리에 매우 친화적인 언어이다 다른 언어에 비해서 왜냐하면 숫자 작업을 도와주는 내장 함수가 많다.
'''

student_scores = [150, 142, 185, 120, 184, 149, 24, 59, 68, 199, 78, 65, 89, 556]

total_exam_score = sum(student_scores)
# print(total_exam_score)

sum = 0
# 합산한 값을 저장하려면 변수가 필요하다 그래서 sum 이라는 변수를 하나 만들어준다.
for score in student_scores:
    sum += score

print(sum)

# max 를 이용해서 위에와 같이 코딩해 최대 값을 출력하라