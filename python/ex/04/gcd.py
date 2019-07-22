"""
求取两个数的最大公约数和最小公倍数

Version: 0.1
Author: 鲁成
"""

a = int(input('请输入一个数：'))
b = int(input('请输入另外一个数: '))

if a > b:
    a, b = b, a

for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print('%d和%d的最大公约数是%d' % (a, b, i))
        print('%d和%d的最小公倍数是%d' % (a, b, ( a * b // i)))
        break
