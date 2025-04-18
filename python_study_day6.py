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
