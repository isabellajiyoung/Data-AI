import random
'''
random.random() #0~1 사이 무작위 실수형 값
print(random.randrange(1,6)) #1~5 사이 무작위 수 출력

chars='한글우수'
print(random.choice(chars)) #저장된 문자열 중 무작위로 문자 출력
'''
pw=str() #pw 이름의 빈 문자열 생성
chars='한글우수'
for i in range(0,5):
    pw += random.choice(chars)
print(pw)
