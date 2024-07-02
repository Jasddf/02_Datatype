#퀴즈1
name = input('이름을 입력하시오 : ')
age = input('나이를 입력하시오 : ')
email = input('이메일을 입력하시오 : ')
phone = input('연락처를 입력하시오 : ')

dic_0 = {name : {'나이':age, '이메일':email, '연락처':phone}}
print(dic_0)

name = input('이름을 입력하시오 : ')
age = input('나이를 입력하시오 : ')
email = input('이메일을 입력하시오 : ')
phone = input('연락처를 입력하시오 : ')

dic_1 = {name : {'나이':age, '이메일':email, '연락처':phone}}
print(dic_1)



#퀴즈2
dic_2 = {'달러' : 1320, '엔' : 950, "위안" : 182}
last = [13,200,13]
x = last[0] * dic_2['달러'] + last[1] * dic_2['엔'] + last[2] * dic_2['위안']

print("철수가 가지고 있는 돈의 원화 가치는" , x , "원입니다.")



