
#list
array = [273, 32, 13, "문자", True, False] #element(요소) 
list_a = [[1,2,3], [4,5,6], [7,8,9]]
print(list_a[0]) #[1,2,3]

#list_index
print(array[0]) #273
print(array[0:2]) #[273, 32]
array[0] = "건물" #요소 변경
print(array)
print(array[3][0]) #문

#list연산자
print(array + list_a)
print(len(array)) #6

#list에 요소추가 (파괴적=원본에변화)
array.append("상우") #요소 추가
print(array)
array.insert(0, "상우") #지정된위치에 요소추가
print(array)
array.extend([3, 4, 5]) #여러개의 요소추가
print(array)
print()
#list에 요소제거
del array[0] #index로 제거
print(array)
array.pop(0) #index로 제거
print(array)
array.remove("문자") #값으로 제거
print(array) 
"문자" in array #False
array.clear() #모두 제거

#for반복문
array = [1,2,3,4,5]
for element in array: #element라는 변수에 array가 들어감
    print(element) #차례로 반복

#dictionary
dict_a = {"a": "b"} #선언, 중괄호, ("a"는 키, "b"는 값)
dict_a["a"] #사용, 대괄호
dict_a["a"] = "ab" #값 변경
dict_a["c"] = "abc" #추가
del dict_a["c"] #제거

#dictionary 내부에 키가 있는 확인하기
dictionary = {"a":"a", "b":"b", "c":"c"}
key = input(">키를 입력하시오: ")
if key in dictionary: #in울 통해 확인
    print(dictionary[key])

#get()함수
value = dictionary.get("d")
print(value) #None

#dictionary + for반복문
for dict_key in dictionary: #dict_key는 키의 변수                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    print(dict_key, ":", dictionary[dict_key])

#range
a = range(5) #선언, range(0,5)
n=10    
range(n/2) #error, 매개변수는 반드시 정수
range(n//2) #정수나누기 연산자 가능

#for(range)
for i in range(5):
    print(i) #0,1,2,3,4


#역반복문
for i in range(4,0-1,-1):
    print(i) #4,3,2,1,0

for i in reversed(range(5)): #reversed()
    print(i) #4,3,2,1,0

#while
list_a = [1,2,1,2]
value = 2
while value in list_a: #True일때
    list_a.remove(value) #반복

#break, continue
    i = 0
    while True: #무한반복
        print("{}번재 반복문입니다.".format(i))
        i += 1
        input_a = input(">종료하시겠습니까?(y/n): ")
        if input_a in ["y", "Y"]:
            print("반복을 종료합니다")
            break #반복종료
        
    numbers = [5,1231,21,321,2]
    for number in numbers:
        if number<10: 
            continue #반복생략
        print(number) #1231, 21, 321

#reversed()
list_a = [1,2,3,4,5]
list_reversed = reversed(list_a) 
print(list(list_reversed)) #list()로 강제변환, 이터레이터이기 때문
for i in reversed(list_a): #필요한 시점에 reversed()사용
    print(i)
list_a[::-1] #확장슬라이싱, reversed()와 같은 기능이지만, 비파괴적

#enumerate() +list
example_list = ["요소A", "요소B", "요소C"]
print(list(enumerate(example_list))) #[(0, '요소A'), (1, '요소B'), (2, '요소C')] #튜플 
for i, value in enumerate(example_list): #반복변수 2개
    print("{}번째 요소는 {}입니다.".format(i, value)) #첫번째{}엔 index, 두번째{}엔 element

#item() +dictionary
example_dicitonary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"}
for key,element in example_dicitonary.items():
    print("dictionary[{}] = {}".format(key,element)) #첫번째{}엔 key, 두번째{}엔 element

#리스트 내포 
array = [i*i for i in range(0,20,2)] #리스트이름 = [표현식 for 반복자 in 반복할수있는것]
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"] #[표현식 for 반복자 in 반복할수있는것 if조건문], !=은 "같음을 확인하는 비교연산자" 

#괄호로 문자열 연결하기
test = (
    "가"
    "나"
    "다") #가나다

#join()으로 문자열 연결하기
"::".join(["1","2","3","4"]) #1::2::3::4, 문자열.join(문자열로 구성된 리스트)

#next()
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)
print(r_num) #오류
print(next(r_num)) #6,
    #이터러블 : 요소들을 차례차례 꺼낼 수 있는 객체 (리스트,딕셔너리 등)
    #이터레이터 : 이터러블 중 next()함수로 꺼낼 수 있는 요소
    #reversed()함수의 리턴값은 이터레이터 -> next()를 이용해서 꺼내야 함