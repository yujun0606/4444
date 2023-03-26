fruits = ['사과', '바나나', '딸기', '키위', '귤', '수박', '사과']
fruits1 = len(fruits)
print(f'과일은 총 {fruits1}개 입니다')
fruits2 = fruits.count('사과')
print(f'사과의 개수 : {fruits2}')
fruits.insert(2, '복숭아')
print(fruits)
if '사과' in fruits:
    print('사과가 과일바구니에 있습니다')
fruits4 = fruits[1 : 4]
print(fruits4)
