import sys
import Person
class AddressBook:

    def __init__(self):
        self.address_list=[]
        self.file_reader()
    
    def file_reader(self):
        try:
            file=open('addressBook.csv','rt')
        except:
            print('addressBook.csv 파일이 없습니다.')
        else:
            while True:
                buffer=file.readline()
                if not buffer:
                    break
                name=buffer.split(',')[0]
                phone=buffer.split(',')[1]
                addr=buffer.split(',')[2].rstrip('\n')
                self.address_list.append(Person(name,phone,addr))
                print('addressBook.csv 파일을 업로드했습니다.')
                file.close()
    
    def file_generator(self):
        try:
            file=open('addressBook.csv','wt')
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write('{},{},{}\n'.format(person.name,person.phone,person.addr))
            file.close()

    def menu():
        print('-'*30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        print('-'*30)
        choice=int(input('수행할 작업을 숫자로 입력하세요>>>'))
        return choice

    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()

    def run(self):
        while True:
            choice=AddressBook.menu()
            if choice==0:self.exit()
            elif choice==1:self.insert()
            elif choice==2:self.delete()
            elif choice==3:self.update()
            elif choice==4:self.search()
            elif choice==5:self.print_all()
            else:print('없는 명령입니다. 확인 후 다시 입력하세요')

    def insert(self):
        print('==신규 주소록 생성==')
        name=input('등록할 이름 입력>>>')
        phone=input('등록할 전화번호 입력>>>')
        addr=input('등록할 주소 입력>>>')
        if name and phone and addr:
            self.address_list.append(Person(name,phone,addr))
            self.file_generator()
            print('신규 주소록이 정상적으로 생성되었습니다.')
        else:
            print('입력값이 부족하여 주소록이 생성되지 않았습니다.')
              
    def delete(self):
        print('==기존 주소록 삭제==')
        name=input('삭제할 이름 입력>>>')
        if not name:
            print('입력된 이름이 없어 삭제를 취소합니다.')
            return
        deleted=False
        for i,person in enumerate(self.address_list):
            if name==self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다'.format(self.address_list[i].name))
                if input('삭제할까요?(Y/N').upper()!='Y':
                    continue
                self.address_list.pop(i)
                deleted=True
                print('{}의 정보를 삭제했습니다.'.format(name))
                self.file_generator()
                break
        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다.'.format(name))

    def update(self):
        print('==기존 주소록 삭제==')
        name=input('수정할 이름 입력>>>')
        if not name:
            print('입력된 이름이 없어 수정을 취소합니다.')
            return
        updated=False
        for i,person in enumerate(self.address_list):
                if name==self.address_list[i].name:
                    print('검색된 전화번호가 "{}"입니다'.format(self.address_list[i].name))
                if input('수정할까요?(Y/N').upper()!='Y':
                    continue
                new_phone=input('변경할 전화번호 입력>>>')
                if new_phone:
                    self.address_list[i].phone=new_phone
                new_addr=input('변경할 주소 입력>>>')
                if new_addr:
                    self.address_list[i].addr=new_addr
                updated=True
                print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요')
                self.address_list[i].info()
                self.file_generator()
                break
        if not updated:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))
    
    def search(self):
        print('===주소록 검색===')
        name=input('찾을 이름을 입력>>>')
        if not name:
            print('입력된 이름이 없어 검색을 취소합니다.')
            return
        for i,person in enumerate(self.address_list):
            if name==self.address_list[i].name:
                print('{},{},{}'.format(self.address_list[i].name,self.address_list[i].phone,self.address_list[i].addr))

    def print_all(self):
        print('==전체 연락처 출력==')
        for person in self.address_list:
            person.info()
        print('총 {}개의 주소록이 있습니다.'.format(len(self.address_list)))