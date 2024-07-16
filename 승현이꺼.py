import random

result=[]
while int(len(result))<6:
    new = random.randint(1,45)
    if new in result :
        print('중복')
    else :
        result.append(new)
print(result)