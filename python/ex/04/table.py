"""
打印九九乘法表

Version: 0.1
Author: 鲁成
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')
    # 打印换行
    print()
