"""
输入年份，如果是闰年输出True，否则输出False


Version：0.1
Author：鲁成
"""

year_input = int(input('请输入年份: '))

is_leap  = (year_input % 4 == 0 and year_input % 100 != 0 or
            year_input % 4000 == 0)
print(is_leap)
