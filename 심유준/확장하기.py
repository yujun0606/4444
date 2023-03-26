# pop : 리스트의 맨 마지막 원소를 리턴하고 해당 원소를 삭제
a = [1, 2, 3]
a.pop()
print(a)

a.pop(1)
print(a)

# index : 위치반환
a = [1, 2, 3]
print(a.index(3))
# extend 확장하기, 리스트 형태로
a = [1, 2, 3]
a = a + [4, 5]
print(a)
