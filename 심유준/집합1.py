# 인덱싱을 위해서는 리스트 혹은 튜플로 반환 하기
a = {1, 2, 3}
b = list(a)
print(b)
print(b[0])
c = {3, 4, 5}
d = tuple(c)
print(d)
print(d[0])
# 집합연산
# 교집합(&, intersection)
# 합집합(|, union)
# 차집합(-, difference)


a = {1, 2, 3, 4}
b = {3, 4 ,5, 6}

print(a & b)
print(a.intersection(b))
print(a | b)
print(a.union(b))
print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))

#값추가 9한개) : add
s1 = {1, 2, 3}
s1.add(4)
print(s1)
#값 여러개 추가 : update
s2 = {4, 5, 6}
s2.update([8,9])
print(s2)
#값 제거 : remove(한개의 값만 지울수있음)
s2.remove(4)
print(s2)
