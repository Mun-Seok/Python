class NameError(Exception):

    def __init__(self, message):
        super().__init__(message)

try:
    name=input('이름을 입력하세요')
    if len(name)<2 or len(name)>6:
        raise NameError('이름은 2~6자 사이로 입력해주세요')
except NameError as e:
    print(e)
else:
    print('입력된 이름은 {}입니다.'.format(name))