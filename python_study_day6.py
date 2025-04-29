'''
day6 
코드블럭과 들여쓰기 대해 살펴보기
함수와 day5에서 배웠던 for 반복문의 다른 기능도 알아보자!
while 반복문에 대해서 알아보자
'''

'''
45.파이썬 함수 정의 및 호출
함수란 무조건 뒤에 () 가 있으면 함수이다.
거의 모든 함수는 동일 한 방법으로 작동한다 ex)print("Hello")

'''
print("Hello")
num_cahr = len("Hello") # 렌 함수를 사용해서 몇 글자인지 확인하고 그걸 저장 하고싶으면 변수에 담아야한다.
print(num_cahr) # 콘솔에서 볼 수 있도록 출력 해준다.

# 함수를 만드는법 

def my_function(): 
    print("Hello")
    print("Bye")

my_function()


'''
변수와 함수를 구분 하는건 괄호이다.() 
그리고 마지막으로 함수의 정의의 아무리는 콜론이다(:)
콜론은 그 줄 뒤에 오는 모든 것과 들여쓰기된 것이 함수에 속한다는 것을 말해 준다.
만든 함수를 호출 하고 싶으면 my_function 을 입력하고 괄호와 필요한 입력값을 추가하는 것이다

def my_function():
    #Do this
    #Then do this
    #Finally do this
위 과정은 첫 단계는 실제로 함수가 무엇을 해야하는 지정(Defining)하는 것이고
이를 위해 먼저 def키워드를 사용한다.
그리고 함수에 이름을 지정한다. 예 my_function 그 다름은 괄호와 콜론이 와야한다.
그리고 나서 이 함수에 포함될 코드 줄을 작성한다. 들여쓰기 필수! 중요
함수를 완성 하고 나서 프로그래밍 용어로는 함수를 호출(Calling)한다고 한다.
함수를 호출하려면 무조건 함수의 이름과 괄호를 지정하면 된다.
'''

#로봇을 움직여 작은 직사각형 만들기
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()


#반복문으로 장애물 넘기
#반복문 중요 많이 쓰이기 때문에 복습 꼭하기
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for step in range(6):
#     jump()

# 파이썬에서의 들여쓰기
''''
들여쓰기 공백에 대한 중요성 대한 이야기
동인한 파일에서 탭과 공백을 혼합하여 들여쓰기에 사용할 수 없다. 파이썬 3부터는.. 이게 맞누?
파이썬 공식 페이지를 가서 PEP 8 -- style Guide 꼭 보기를 추천한다..
'''

# while 반복문
'''
while loops = 특정 조건이 참일 경우 명령이 게속 실해되는 반복문
'''

# For 

# for item in list_of _iems:
#     #Do something to each item

# for number in range(a, b):
#     print(number)

#While

# while something_is_true
#     #Do something repeatedly

# wheile 사용한 로봇 게임
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

#while 사용방식
# while something_is_true:
    #Do this
    #Then do this
    #Them do this

# number_of_hurdles = 6
# while number_of_hurdles > 0: # while something_is_true: 이 부분과 같다
#     jump() 
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# reeborg 허들 경주(while를 사용해서 만들기기)
# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()
    
# def jump():
#      move()
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()
    
# #number_of_hurdles = 6
# while number_of_hurdles > 0:
#    jump()
#    number_of_hurdles -= 1
#    print(number_of_hurdles)
    
# while not at_goal():
#     jump()
#     if at_goal(): 
#         break
'''
허들 경주
리보그가 허들 경주에 참가했지만, 경주 시간이 얼마나 될지 미리 알지 못합니다. 표시된 경로와 비슷한 경로를 따라 달리되, 경주가 시작된 후 표시되는 유일한 깃발에서 멈추도록 하세요.
당신이 알아야 할 것
기능 move()과 turn_left().
조건 at_goal()과 그 부정.
루프 를 사용하는 방법 while.
귀하의 프로그램은 세계 허들 1 에도 유효해야 합니다 .
'''
'''
for 반목분도 배우고 while 반복문도 배웠는데
둘을 모두 사용할 수 있다면 왜 어느 한쪽을 선택해야 하지?
for 반복문과 while 반복문은 각각 언제 사용해야 할까?
= for 반복문의 경우 어떤 것을 반복하고 반복하는 각 아이템에 대해 뭔가를 해야 할 때 유용하다.
예를 들자면 어떤 리스트를 반복하는데 '과일들'이라는 리스트에 있는 각 과일에 대해 뭔가를 하길 원하죠 거죠
여기 있는 아이템들에 대해서.. 간다한 반복문을 출력해야 하는 경우 for 반복문을 써야 한다
fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
    print(fruit)
이런 경우 간단한 리스트를 반복할때 이럴때 while 반복문을 사용하면 이 작업은 쉽지 않다.
수열 함수도 있기 때문에..(range)함수를 말한다 (1 ~ 6의 범위 안의 각 번호를 호출하는 식으로로)
for 문과 range 같이 사용하기 편함!

한편 while 반목문의 경우 전체 순서에서 몇번째에 해당하는지 어떤 아이템을 반복하지가 아닌, 그저 특정 작업을
설정한 조건에 도달할 때까지 수없이 반복 수행하고자 할 때 많이 사용한다.

참고로 while 반복문은 for 반복문에 비해 약간의 위험성이 있다, 왜냐하면 for 반복문은 실행 횟수를
사전에 설정해두기 떼문에 이 경우에는 리스트가 끝나면 실행이 중단되고 이 경우의 범위의 상한선에 이르면
중단 되지만 while 반복문의 경우 특정 조건이 거짓으로 전환될 때까지 계속 실행되기 때문에 만약 조건이 
거짓이 되지 않는다면 소위 무한 반복이라 불리는 반복문이 된다.
예를 들면 
while 5 > 3:
    #do this
    #Then do this
    #Then do this
5가 3보다 크다는 것은 영원한 진리이기 때문에 이코드 또한 영원히 실행된다는 의미가 된다.
이경우 printf를 사용해서 디버깅을 꼭 해보는게 아주 중요하다!!!**
''' 

# while 반복문을 사용한 장애물 넘기
'''
허들 경주
리보그가 허들 경주에 참가했습니다. 표시된 경로를 따라 코스를 달리게 하세요.

이 세계를 다시 로드할 때마다 허들의 위치와 개수가 변경됩니다.
당신이 알아야 할 것
기능 move()과 turn_left().
조건 front_is_clear()또는 wall_in_front(), at_goal(), 그리고 그 부정.
while루프와 명령문을 사용하는 방법 if.
귀하의 프로그램은 세계 허들 1 과 허들 2 에도 유효해야 합니다 

front_is_clear() = 앞이 비어 있거나 
wall_in_front() = 앞에 벽에 있거나
at_goal() = 목표에 도달한 경우와 그 부정문인 앞이 비어 있지 않은 경우, 앞에 벽이 있지 않은 경우
목적지가 아닌 경우 이전에 배운 not과 while 반복문을 사용해서 문제를 풀어보자!

허들 넘기 정답
def turn_right():
     turn_left()
     turn_left()
     turn_left()
    
def jump():
#    move()
     turn_left()
     move()
     turn_right()
     move()
     turn_right()
     move()
     turn_left()
    
#number_of_hurdles = 6
#while number_of_hurdles > 0:
#    jump()
#    number_of_hurdles -= 1
#    print(number_of_hurdles)
    
#while not at_goal():
#    jump()
#    if at_goal(): 
#        break

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''