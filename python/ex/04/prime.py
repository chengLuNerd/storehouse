"""
判断一个数是否是素数

Version: 0.1
Author: 鲁成
"""

import math

number = int(input('请输入一个数：'))

is_prime = True
end = int(math.sqrt(number))

for i in range(2,  end + 1):
    if number % i == 0:
        is_prime = False
        break
        
if is_prime and number != 1:
    print('%d是素数'% number)
else:
    print('%d不是素数'% number)
    
