fruits = []

name = input("좋아하는 과일 이름을 입력하세요 :")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하세요 :")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하세요 :")
fruits.append(name)
name = input('과일의 이름을 입력하세요 :')
if name in fruits:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 싫어하는 과일입니다.")
