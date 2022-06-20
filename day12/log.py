def log(input):
    with open('log.txt','at',encoding='UTF-8') as file:
        file.write(input)