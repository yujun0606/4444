# 이중for문
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for back in b:
    for front in a:
        print(f'{back} * {front} = {back * front}')
