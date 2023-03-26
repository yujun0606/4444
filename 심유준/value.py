my_dic = {'one' : 1, 'two' : 2, 'three' : 3,}

# key로 value찾기
print(my_dic.get('two'))

# key를 다 뽑아서 list로 만들기
a = my_dic.keys()
b = list(a)
print(b)

#value를 다 뽑아서 list로 만들기
c = my_dic.values()
d = list(c)
print(d)
#key, value를 덩어리로 다 뽑기
print(my_dic.items())
#모두 삭제하기
print(my_dic.clear())

