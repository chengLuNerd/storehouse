"""
从一段文字中提取出手机号段

Version：0.1
Author：cheng.lu
"""

import re

def main():
    #创建正则表达式对象
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''

    """
    my_list = re.findall(pattern, sentence)
    print(my_list)
    """

    for temp in pattern.finditer(sentence):
        print(temp.group())


if __name__ == '__main__':
    main()
