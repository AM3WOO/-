#Boolean
print(10==10) #True
print(10<=100) #True
print(10!=10) #False, !=(다르다)
print("가방"<"하마") #True, 사전순서
x = 25
print(20<x<30) #True
print()
#not, and, or (논리연산자)
print(not True) #False
x = 10
under_20 = x < 20
print(not under_20) #False
print(True and True) #True
print(True or False) #True

#if조건문
number = input("정수입력 : ")
number = int(number)
if number>0 :
    print("양수입니다")
if number==0 :
    print("0입니다")
if number<0 :
    print("음수입니다")

#오전과 오후를 구분하는 프로그램
import datetime
now = datetime.datetime.now()
if int(now.hour) < 12 :
    print("현재 시각은 {}시로 오전입니다".format(now.hour))
else :
    print("현재 시각은 {}시로 오후입니다".format(now.hour))

#홀수와 짝수를 구분하는 프로그램1
number = input("정수를 입력하시오: ")
last_character = number[-1] #끝자리 가져오기
if last_character in "02468" :
    print("짝수입니다")
else :
    print("홀수입니다")

#홀수와 짝수를 구분하는 프로그램2
number = input("정수를 입력하시오: ")
number = int(number) #숫자화
if number % 2 == 0 : #나머지로 짝수 구분
    print("짝수입니다")
if number % 2 == 1 : #나머지로 홀수 구분
    print("홀수입니다")

#elif 사용해 조건문 구현하기
grade = float(input("학점을 입력하시오"))
if grade == 4.5 :
    print("신")
elif 4.2<= grade : #상위값은 검사생략
    print("교수님의 사랑")
elif 3.5<= grade :
    print("현 체제의 수호자")
elif 2.8<= grade :
    print("일반인")
elif 2.3<= grade :
    print("일탈을 꿈꾸는 소시민")
else :
    print("불가촉천민")

#pass 키워드
number = int(input("정수입력 : "))
if number > 0:

    pass
else:

    pass #아무것도안했고, 나중에 개발하겠음이라는 뜻