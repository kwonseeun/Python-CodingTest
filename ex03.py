members = {}
while True:
    menu = input ('회원정보 추가(a), 검색(f), 수정(u), 삭제(d), 목록(s),종료(x): ')
    if menu =='a':
        name = input ('이름 입력:').title()
        phone = input('전화번호 입력:') 
        members[name] = phone
        print('-------------------')
        print(f'*****{name} 입력 완료*****')
        print('-------------------')
        
    elif menu =='f':
        name = input('검색할 이름 입력:').title()
        phone = members.get(name, '존재하지 않습니다.')
        print('--------------------')
        print(f'{name}:', phone)
        print('--------------------')
         
    elif menu=='u':
        name = input ('수정할 이름 입력:').title()
        if name not in members.keys():    
            print('-----------------')
            print(f'{name} 회원은 존재하지 않습니다.')
            print('-----------------')

    elif menu=='d':
        name = input ('삭제할 이름 입력:').title()
        if name not in members.keys():
            print('------------------')
            print(f'{name} 회원은 존재하지 않습니다.')
            print('------------------')
            continue
    else:
        ask = input(f"{name} 회원을 정말로 삭제할까요?(y)").lower()
        if ask == y :
            del member[name]
            print('-----------------')
            print(f"******{name} 삭제 완료*******")
            print('-----------------')
        else:
            print('-----------------')
            print(f'{name} 회원을 삭제하지 않았습니다.')
            print('-----------------')
 