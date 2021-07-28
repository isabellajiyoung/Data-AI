# 1. 파이썬에서 기본으로 제공하는 함수
print()
range()
type()

# 2. 그보다 더 많은 기능들을 제공해주는 모듈 (함수라기보다는 객체지향 개념으로 메소드라고 함)
# 객체.메소드()
# ex. import math
#     math.sqrt()


# 3. 사용자 정의 함수
def hello():
    print('Hello!')
hello()

def add(a,b):
    sum = a+b
    return sum #기능a+b에 따라 수행한 값이 변수sum에 저장
print(add(1,3)) #return은 결괏값 sum을 함수를 호출한 print로 반환
result=add(1,3)
print(result)

def add_sub(a,b):
    sum=a+b
    diff=a-b
    return sum, diff #기능 2개, 변수 2개, 결괏값 2개
print(add_sub(1,3))

def swap(a,b):
    return b,a
a=3
b=5
a, b=swap(a,b)
print('a=',a, 'b=',b)

