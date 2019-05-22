import random
a=random.randint(0,9)
b=int(input("好きな数字を入力してください(1~9):"))
if a==b:
    print("正解です！")
else:
    print("不正解です")

print("答えは:"+str(a))
print("あなたの入力した数値は:"+str(b))
