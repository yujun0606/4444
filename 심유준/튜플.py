'''colors = ('red', 'blue', 'green')
print(colors)
print(type(colors))
print(colors[0])
print(colors[ : ]) #튜플로 글라이싱 했을 떄 튜플로 반환

#예제1
str_data = ('르세라핌', '트와이스', '세븐틴', '엑소')
print(type(str_data))
print(str_data[-1])

str_data = str_data + ('뉴진스',)
print(str_data)

str_data = str_data + ('레드벨벳', '러블리즈')
print(str_data)'''

# 예제2
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = ('orange', 'melon', 'straberry')

tuple3 = tuple1 + tuple2
print(tuple3)

#tuple1의 요소만 추출하기
for x in tuple1:
    print(x)

#tuple3의 길이 구하기
print(len(tuple3))

#예제3
my_tuple = (1, 2, 2, 2, 3, 3, 4, 5)
print(my_tuple.count(3))
print(my_tuple.index(4))
print(len(my_tuple))
print(min(my_tuple))
print(max(my_tuple))
print(3 in my_tuple)
print(4 not in my_tuple)


