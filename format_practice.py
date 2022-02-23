#format() 함수로 숫자열을 문자열로 변환
format_a = "{}열공하여 {}만원 만들기".format("파이썬", 5000)
print(format_a)

#format()함수 다양한 기능
output_a = "{:d}".format(52) #정수
output_b = "{:5d}".format(52) #특정칸에 출현
output_c = "{:05d}".format(52) #빈칸을0으로 채우기
print(output_a)
print(output_b)
print(output_c)

#{:f}으로 float자료형 지정
float_a = "{:f}".format(52.1743)
float_b = "{:15f}".format(52.1743) #15칸 만들기
float_c = "{:15.2f}".format(52.1743) #15칸 만들고, 소수점자리 지정
print(float_a)
print(float_b)
print(float_c)