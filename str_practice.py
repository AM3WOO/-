#index (slicing)
print("안녕하세요"[0]) #안 (indexing)
print("안녕하세요"[0:3]) #안녕하 (slicing)
print("안녕하세요"[:3]) #안녕하 (slicing)

#len (문자열의 길이)
print(len("안녕하세요"))

#복합대입연산자
number = 100 #100
number *= 10 #1000
print(number)
string = "안녕하세요"
string +="!" #string = string + "!"
print(string)

#upper()와 lower()함수
a = "Hello Python Programming"
print(a.upper()) #대문자화
print(a.lower()) #소문자화

#strip()함수
strip_a = '''
        안녕하세요
문자열의 함수를 알아봅시다
'''
print(strip_a.strip()) #공백제거

#in연산자
print("안녕" in "안녕하세요") #True
print("잘가" in "안녕하세요") #False
