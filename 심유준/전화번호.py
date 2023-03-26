#ch12lab4.py
num = input('전화번호를 입력하세요 :')
num = num.replace('-','')
print(f"전화번호 : {num}")
print(f'전화번호 끝 4자리 {num[-4 :]}')
