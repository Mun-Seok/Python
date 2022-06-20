from updown1 import updown as check
import random
import log

max=100
min=1
count=0
print('UP Down 게임입니다')
answer=random.randint(1,100)
while(True):
    user_input=int(input('{}부터 {}사이의 숫자를 입력해 주세요>>>'.format(min,max)))
    result,max,min=check(user_input,answer,max,min)
    if result==1:
        print('정답입니다.')
        break
    else:
        print(result)
    count+=1
    state='play count: {},input value:{}, answer: {},max: {},min: {}\n'.format(count,user_input,answer,max,min)
    log.log(state)