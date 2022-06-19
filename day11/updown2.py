from updown1 import updown as check
import random
from datetime import *

max=100
min=1
print('UP Down 게임입니다')
answer=random.randint(1,100)
start=datetime.now()
while(True):
    user_input=int(input('{}부터 {}사이의 숫자를 입력해 주세요>>>'.format(min,max)))
    result,max,min=check(user_input,answer,max,min)
    if result==1:
        print('정답입니다.')
        end=datetime.now()
        t=end-start
        t=t.total_seconds()
        print('{}초가 걸렸습니다'.format(t))
        break
    else:
        print(result)