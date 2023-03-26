zoo = ['곰', '강아지', '고양이', '사자', '호랑이', '여우', '늑대', '원숭이', '뱀', '코끼리']
like = []
hate = []
for x in zoo:
    an = input(f'{x} 좋아하세요?')
    if an =='네':
        like.append(x)
    else:
        hate.append(x)
print(f'좋아하는 동물들 : {like}')
print(f'싫어하는 동물들 : {hate}')

