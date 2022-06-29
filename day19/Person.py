import sys

class Person:

    def __init__(self,name,phone,addr):
        self.name=name
        self.phone=phone
        self.addr=addr
    
    def info(self):
        print('{},{},{}'.format(self.name,self.phone,self.addr))
