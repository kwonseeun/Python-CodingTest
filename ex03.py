members = {}
while True:
    menu = input ('회원정보 추가(a), 검색(f), 수정(u), 삭제(d), 목록(s),종료(x): ')
    if menu =='a':
        name = input ('이름 입력:').title()
        phone = input('전화번호 입력:') 
        members[name] = phone
        print('------------')
        print(f'*****{name} 입력 완료*****')
        print('------------')