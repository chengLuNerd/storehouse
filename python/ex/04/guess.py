"""
猜数游戏


Version：0.1
Author：鲁成

"""

import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input("please input: "))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了!")
        break

print("你一共猜了%d次" % counter)

if counter > 7:
    print("你的智商余额明显不足")


