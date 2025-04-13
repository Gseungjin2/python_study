# day3 무작위화 및 파이썬 리스트

# Random 모듈
# 의사난수 생성 수학이 많다 그리고 파이썬ㅇ이 사용하는 것은 메르센 트위스터(Mersenne Twister) 라고불리는 것이다.

import random
import my_module

# random_integer = random.randint(1, 10)
print(random_integer)

# #모듈 만들고 쓰는법 동작 방식식
print(my_module.my_favourite_number)

# Module 이란 
"""
우리가 대부분의 코드를 일종의 스크립트 스타일로 같은 페이지에 작성해 
왔다는 것을 봤을것이다. 모든 코드가 위에서 아래로 실행된다. 하지만
때로는 복잡한 것을 만들려고 할 때 코드가 너무 길어져서 큰 코드 덩어리
에서 무슨 일이 일어나고 있는지 이해할 수 없게 됩니다. 그런 경우 사람들은
코드를 개별 모듈로 나누어 각 모듈이 프로그램의 서로 다른 기능을 담당하게
한다. 그리고 많은 모듈이 있는 복잡한 프로젝트가 있다면 다른 사람과 협업할
수도 있다. 많은 사람들이 각기 다른 작업을 할 수 있다.예를 들어 공장에서
한 사람이 바퀴에서 차죽, 자체 까지 전체 자동차를 만드는 것은 말이 안된다.
대신 타이어 모듈, 자체 모듈, 엔지 모듈 등 서로 다른 사람들이 가가 작업한 후
모든 것을 조립하면 최종 자동차, 즉 우리의 경우 최종 프로그램이 완성됩니다.
그래서 random 모듈은 의사 난수를 생성하는데 필요한 모든 복잡한 수학을 거치지
않고도 임의 숫자를 쉽게 생성할 수 있도록 파이썬에서 만드 모듈이다.
"""

import random

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)



"""
random.random 첫번째 랜덤은 모듈이고 . 뒤 두번째 함수를 말한다. 
항상 () 처서 함수를 활성화 시켜야한다 ()는 이것이 무엇을 출력할지, 
입력 프롬프트가무엇인지 또는 무작위 정수의 범위가 무엇인지와 같은
입력을 넣기 위해 사용된다. 하지만 일부 함수는 전형 입력 받지 않는다.
그래도 여전히 함수에는 괄호 세트가 필요하다 

* 10 를 같은거를 사용하여 확장할 수 있다 위 함수에 10을 곱하면 생성된
숫자가 0과 10 사이가 되지만, 10은 포함하지 않는다. 왜냐하면 하한인 0을
10으로 곱하면 0이 되고 상한인 1을 10으로 곱하면 10이 되기 때문에이다
그래서 이 난수 생성기를 0과 우리가 원하는 값 사이에서 부동 소수점 숫자를
생성하도록 변경했다.

그래서 다른 함수인 부동 소수점 난수 생성기가 따로 존재한다.
위 부동 소수점 난수 생성기를 실행하면 위에 * 10을 한 값다 동일한 값을
만들어낸다 유일한 차이점은 반올림에 따라 10이 나올지 안 나올지 확실하지
않다는 것이다. 따라서 범위를 확실 하기 위해서 반 개방혀 범위라고 불리는
random.random을 사용하여 항상 0을 포함하지만 1을 결코 포함하지 않을 수
있다. 그 사실을 알고 있다면 * 를 사용해서 원하는 대로 사용할 수 있다.
"""

# 동전 앞면 또는 뒷면을 출력하는 프로그램 미니 프젝
import random

randmom_heads_or_tails = random.randint(0, 1)
if randmom_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# 오프셋(대충 인데스로 이해하기기)을 이해하고 리스트에 항목 추가하기
"""
리스트는 데이터 구조이다(Data Structure)
0은 맨앞 첫번째 -1은 맨끝에서 첫번째 -0은 없다
"""

status_of_america = ["Delaware", "Pennsylvania, New jersey"]

print(status_of_america[0])

status_of_america.append("Seungjin") 
status_of_america.extend(["Srungjin", "Seungin2", "Seungjin3"])
# append 함수는 리스트 맨끝에 항목을 추가할 수 있는지 내장 함수이다. extend 함수를 사용하면 맨끝어 여러 항목을 한번에 추가 할수있다다

status_of_america[1] = "Pencilvania" # 인덱스를 사용해서 이런씩으로 특정 내용을 수정할 수 있다.ㄴㄴ
print(status_of_america)

# 금융가 룰렛 - 누가 계산해야 할까요? 미니 프젝
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
Russian_Roulette = random.choice(friends)
print(Russian_Roulette)

# 강의 정답
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])

"""
1. 리스트에서 1개만 랜덤 추출하기
리스트의 요소를 추출하는 함수는 choice 와 sample 이 있습니다. 두 가지가 차이점이 있겠죠? 
먼저 choice는 리스트에서 한 가지 요소만 랜덤으로 추출하는 함수 입니다.
"""

# IndexError 및 중첩 리스트 활용하기

status_of_america = ["Delaware", "Pennsylvania, New jersey", "Georgia"] # 50개의 주라고 했을때 

# print(len(status_of_america))

num_of_status = len(status_of_america) # 50 -> 49

# print(num_of_status)

print(status_of_america[num_of_status - 1]) # 이런씩으로 사용해야함

"""
위 print문을 그냥 사용하면 리스트 인덱스 범위 초과 오류가 나옴 재대로 출력하긴 위해서 -1 필요
"""
# 중첩 리스트

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_doaen = [fruits, vegetables]
print(dirty_doaen[1][1])

"""
kale 나오는 이유는 중첩 리스트 순차적으로 확인하고 첫번째 인데스도 확인하지만 건너뛰고 마지막 인덱스를 확인한뒤 마지막 
인덱스인 kale 만 나오는걸 확인하였다다
"""

# 4일차 프로젝트: 가위바위보
# 강의 영상 정답 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

import random

game_images = [rock, paper, scissors]

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choise])

Computer_chose = random.randint(0, 2)
print("Computer chos")
print(game_images[Computer_chose])

if user_choise >= 3 or user_choise < 0:
    print("You typed an invalid number. You lose!")
elif user_choise == 0 and Computer_chose == 2:
    print("You win!")
elif Computer_chose == 0 and user_choise == 2:
    print("You lose!")
elif Computer_chose > user_choise:
    print("You lose")
elif user_choise > Computer_chose:
    print("You win!")
elif Computer_chose == user_choise:
    print("It's a draw!")