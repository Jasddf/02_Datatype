#리스트(집합)
Ys = ['장영수', '29', '010-8711-9415']
name = Ys[0]
age = Ys[1]
phone = Ys[-1]
print(Ys, type(Ys))
print(name, age, phone)

names = [["장영수", "한별", "이상우"],['29', '27', '29'],['010-8711-****', '010-7280-****','010-3320-****']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[4]
print(result)

print(len(names[0]))

#리스트에 요소 추가하기
last = [1,2,3,4]
last.append(30)
print(last)
last.remove(3)
print(last)
print(type(last))

#딕셔너리(key-value데이터)
dic = {'장영수' : 29, '이상우' : 29}
dic['장영수'] = 30
print(dic['장영수'])

dic_2 = {'장영수' : [29, 173, 71, '010-8711-****'], '이상우' : [29, 183, 75, '010-3320-****']}
dic_3 = {'장영수' : {'나이' : 29, '키' : 173, '몸무게' : 71, '연락처' : '010-8711-****'}}

print(dic_2['장영수'])
print(dic_3['장영수']['키'])