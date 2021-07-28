
num=3.2
print('출력:',num)
print(1,2,3,4,5) # 정수형 값을 출력
print('1','2','3','4','5') # 문자열형 값을 출력

name=input('이름:')
print(name)
# input()으로 입력받으면 문자열로 저장되기 때문에 계산을 하려면 정수형으로 변환해주어야한다.
age=input('나이:')
print(int(age)+10)
old=int(age)+10 # 더하기 해주려면 문자열형+문자열형 혹은 정수형+정수형 이어야 한다.
print(old)
type(age)



#조건문
num=-1
if (num>0):
    print('양수')
elif (num<0):
    print('음수')
else:
    print('0')



#반복문
for i in range(3):
    print(i)
    print('안녕!')
    
for i in range(2,5):
    print(i)
    print('안녕하세요!')

for i in range(6,-1,-3): #범위는 6부터 0까지
    print(i,end='') #반복문은 기본적으로 줄바꿈(개행)되는데 end=''를 붙여주면 한줄에 출력됨.

for i in range(1,10):
    print('[',i,'단',']')
    for j in range(1,10):
        print(i,'*',j,'=',i*j)
    print('\n')

sum=0
for i in range(100):
    sum += i
    if (sum>100):
        break #for문 내에서 반복을 수행하다가 if문의 조건식을 만족하면 break를 실행하여 그 반복문을 벗어나게 하는 프로그램
print(sum, i)

sum=0
for i in range(100):
    if (sum>100):
        continue # continue는 for문이나 while문 안에서 반복 수행을 하다가 continue를 만나게 되면 그 이후의 명령문은 실행하지 않고 반복문의 처음으로 돌아가도록 하는 명령어이다.
    sum += i
print(sum, i) #0에서 100보다 적을 때까지의 값들을 차례로 더하다가 그 합이 100보다 커지면 더 이상 더하지 않도록 하는 프로그램

