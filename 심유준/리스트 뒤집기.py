# 리스트 응용2
# 리스트 뒤집기 : reverse
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)

# 정렬 : sort, 기본적으로 오름차순 정렬
list2 = [3, 5, 2, 1, 7]
list2.sort()
print(list2)

# 내림차순 (reverse = True)
list3 = [3, 2, 1, 5, 4]
list3.sort(reverse = True)
print(list3)

# 알파벳 정렬
list4 = ['banana', 'carrot', 'apple']
list4.sort()
print(list4)
list4.sort(reverse = True)
print(list4)
