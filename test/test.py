#coding=utf-8
import itertools as its
import random
import string
# a=[1,2,3];
# b=[4,5,6];
# a = '不行;广大;大幅度;老;充分;大钱;大规模;特大;爸爸;俊雅;可怜;死;杀'.split(';')
# b = '常温;超低温;高温;恒温;候温;炉温;气温;室温;水温;体温'.split(';')
# print("a,b的笛卡尔乘积：")
# for x in itertools.product(a,b):
#     print(x[0], x[1])
# print()
# print("a自身的笛卡尔乘积：")
# for x in itertools.product(a,a):
#     print(x[0], x[1])

# import time
#
# def get_time(type=None):
#     if type == None:
#         nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     else:
#         nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#     print('Time: ',nowtime)
#     return nowtime

import  itertools,string
import sys

# 获取数据
def dict(num,bad):
    words = "0123456789"
    # words = string.digits

    r = its.product(words, repeat=num)
    for i in r:
        # 去重
        if len(set(i)) != num:
            continue
        #去除指定数字
        result = ''.join(i)
        if result.__contains__(str(bad)):
            continue
        print(result)

def dicts(num,bad,times):
    for i in range(times):
        dict(num,bad)

def readdata():
    result = []
    for i in range(2):
        line = sys.stdin.readline().strip()
        data = line.split(' ')
        result.append(data)
    return result


if __name__ == '__main__':
    data = readdata()
    dicts(int(data[0][0]),data[0][1],int(data[1][0]))

