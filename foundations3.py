#문자열string과 배열sequence

print('hello')
print("hello")
print('She said, "oh!"')
print("I thought 'it is ridiculous'")

#문자열string
animal='frog'
print(animal[3]) #g

fruit='orange'
print(fruit[2]) #a
print(fruit[-4]) #a

dog='개'
animal='진돗'+dog #문자열의 병합
print(animal)

animal='elephant' #animal이라는 변수에 문자열'elephant'를 입력하면 자동으로 animal이라는 문자열 객체가 생성
print(len(animal)) #문자열(객체)의 길이를 반환 #8
print(animal.count('e')) #animal이라는 객체 안에 count라는 메소드를 점으로 연결하여 호출
print(animal.find('e'))
print(animal.find('ep'))
print(animal.rfind('e'))
print(animal.index('e'))
print(animal.startswith('el'))
print('n' in animal) #True
print('an' in animal) #True
print('an' not in animal) #False

ai='python program'
print(ai.replace('p','P'))
print(ai.lower()) # 소문자
print(ai.upper()) # 대문자
print(ai.swapcase())
print(ai.capitalize()) # 이것들은 '화면에 출력만' 하는 것이지 원래 저장된 내용을 수정하는 것은 아님

animal='Elephant'
animal=animal.upper() # 메소드를 이용해 '저장된 내용을 수정'
print(animal)
print(animal.lstrip()) # 문자열의 왼쪽 공란들을 삭제
print(animal.rstrip()) # 문자열의 오른쪽 공란들을 삭제
print(animal.strip()) #문자열의 좌우 공란들을 삭제







# 배열: 문자열형, 유니코드 문자열형, 리스트, 튜플, 바이트배열, xrange와 같은 배열형 자료구조
# 한 개의 변수로 다수 개의 데이터를 저장해 두고 편리하게 접근하고자 하는 목적
# 변경가능한(mutable): 리스트형, 사전형, 집합형
# 변경할 수 없는(immutable): 숫자형, 부울형, 문자열형, 튜플형

# 리스트
price=[1020, '사과', 0.23587] #리스트에서는 하나의 공간에 정수, 실수, 문자열이 모두 입력될 수 있다. 

x=12.23
y=23.34
packing=[x,y] #packing
print(packing)
[c1, c2]=packing #unpacking
print(c1, c2)

fruits1=['apple','orange','grape']
fruits2=['banana','blueberries']
allfruits=fruits1+fruits2 #리스트의 병합
print(allfruits)



#리스트에 원소를 삽입하는 3가지 방법
# 1. append() '마지막에 추가'
prime=[2,3,5]
prime.append(7)
print(prime) #[2,3,5,7]

a=list()
for i in range(0,5):
    a.append(i)
    print(a[i])

# 2. insert() 2개의 입력인자. 첫번째는 인덱스 번호이며 해당 인덱스 번호 직전의 위치에 두 번째 인자의 값을 입력하라는 의미
fruits=['apple','orange','grape']
fruits.insert(1,'blueberries') 
print(fruits) #['apple','blueberries','orange','grape']

# 3. 리스트의 함축
mylist=[3,5,4,9,1,8,2,1]
newlist=[i for i in mylist if (i%2)==0] 
print(newlist)




#리스트의 항목을 부분적으로 삭제하기 위한 3가지 방법
# 1. del 명령문
nums=[0,1,2,3,4,5]
del nums[1]
print(nums) #[0,2,3,4,5]

nums=[0,1,2,3,4,5]
del nums[1:5] #슬라이싱 기능도 사용 가능
print(nums) #[0,5]

# 2. 리스트(객체)에서 제공하는 메소드 pop()
nums=[1,3,5,7,9]
nums.pop() #입력 인자를 입력하지 않으면 리스트의 마지막 행이 삭제된다. 
nums.pop()
nums.pop(2) #입력값을 넣어주면 인덱스로 인식한다!!!
print(nums) #[1,3]

# 3. 빈 리스트[]로 삭제
nums=[0,1,2,3,4,5]
nums[1:2]=[]
print(nums) #[0,2,3,4,5]




#존재여부(Checking Membership)
word='orange'
print('r' in word) #True

fruits=['사과','오렌지','포도']
print('포도' not in fruits) #False




#원소의 반복
a=[1,2,3]
b=a*2
print(b) #[1,2,3,1,2,3]

a=[1,2,3]
for i in a:
    print(i*2) 
'''
2
4
6
'''
a=[1,2,3]
for i in a:
    print(i*2,end='') #2,4,6 



#원소의 개수 측정
fruits=['apple','orange','grape']
print(len(fruits)) #3



#빈도수 검사(검색 기능)
nums=[5,7,1,3,5,7,1,3,3,5,7,9]
print(nums.count(5)) #3



#인덱스 번호 찾기
nums=[1,2,3,4,5,3]
print(nums.index(3)) #리스트에서 3이 처음 나오는 인덱스의 번호를 반환 #2





#정렬(Sorting)
nums=[3,5,2,1,5,3]
nums.sort() #오름차순으로 정렬(입력값 없이 사용)
print(nums) #[1,2,3,3,5,5]

nums=[3,5,2,1,5,3]
nums.sort(reverse=True) #내림차순으로 정렬(reverse=True 옵션 사용)
print(nums) #[5,5,3,3,2,1]




#2차원 리스트
fruitdb=[['apple',1020],['orange',880],['grape',3160]] #3개의 리스트 원소를 가지는 리스트
print(fruitdb[1]) #['orange',880]
print(fruitdb[1][0]) #orange

record=[ [1,2,3],[10,20,30],[100,200,300] ]
index = [ary[1] for ary in record]
print(index) #[2,20,200]

mylist=[ [1,2],[3,4,5],[6,7] ]
newlist= [x for x in mylist if len(x)==2]
print(newlist) #[[1,2],[6,7]]




#튜플(변경불가)
empty=() #빈 튜플을 생성 empty=tuple()
animals=('토끼','사자','원숭이')
fruits='사과','오렌지',1020,880
start='하나','둘',
print(fruits)
print(fruits[1]) #indexing
print(fruits[1:3]) #slicing

animals = ('토끼','사자','원숭이')
fruits = '사과','오렌지',1020,88,
things = animals, fruits #튜플은 튜플을 원소로 가질 수 있으며 리스트와 마찬가지로 2차원적인 구성을 만들 수 있다. 
print(things) #(('토끼','사자','원숭이'),('사과','오렌지',1020,88))


#딕셔너리 { 키key : 값value } 딕셔너리에는 순서라는 게 없으므로 인덱싱과 슬라이싱이 먹히지 않는다. 
student={} # 빈 사전을 생성함. student=dict()
student['지훈']=1234 # 딕셔너리는 숫자로 리스트나 튜플처럼 숫자로 색인(인덱싱)하지 않고 키(key)를 인덱스처럼 사용한다. 
print(student) # {'지훈':1234}

student['수민']=2345
print(student) # {'지훈':1234,'수민':2345}
print(student['지훈']) # 1234


#집합 {} 사전과 달리 키만 있고 값이 없는 형식! 집합은 add(),update(),remove(),pop()메소드를 이용해 수정이 가능하다.
dict = {} #빈 사전을 생성 또는 dict=set()
dict = {3,2,3,1} #중복된 원소를 포함한 데이터 입력
print(dict) # {1,2,3}

fruits = ['apple','orange','grape','orange']
fruits = set(fruits)
print(fruits) #{'orange','apple','grape'}




