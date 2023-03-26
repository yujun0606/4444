# 딕셔너리 (키와 값)

'''
1. 키는 중복일 수 없다.
2. 키가 있어야 값을 알 수 있다.
3. 값만 안다고 해서 키를 알 순 없어.
4. **인덱싱 불가 
'''

phone = {}
phone['심유준'] = '010-1111-2222'
phone['심유준'] = '010-1111-2222'
print(phone)

#딕셔너리 (키와 값)
my_dic = {'one' : 1, 'two' : 2}
# 값 변경
my_dic['one'] = 10
print(my_dic)
# 새로운키와 값추가
my_dic['three'] = 3
print(my_dic)
# 삭제(del)
del my_dic['one']
print(my_dic)
#key가 딕셔너리에 있는지 확인
if 'two' in my_dic:
    print('있습니다.')
# value가 딕셔너리에 있는지 확인
if 10 in my_dic:
    print('있습니다')
else:
    print('없습니다')

