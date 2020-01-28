import itertools

'''
python列表解析（[ x for x in list]）
>Python 的强大特性之一是其对 list 的解析，它提供一种紧凑的方法，
可以通过对 list 中的每个元素应用一个函数，从而将一个 list 映射为另一个 list。
>列表解析，又叫列表推导式( list comprehension)
>列表解析比 for 更精简，运行更快，特别是对于较大的数据集合
>列表解析可以替代绝大多数需要用到 map和 filter的场合

列表推导式提供了一个创建链表的简单途径，无需使用 map() ， filter() 以及 lambda 。
以定义方式得到列表通常要比使用构造函数创建这些列表更清晰。每一个列表推导式包括在一个 for 语句之后的表达式，
零或多个 for 或 if 语句。返回值是由 for 或 if 子句之后的表达式得到的元素组成的列表。如果想要得到一个元组，
必须要加上括号。

'''

# 基本用法
[x for x in range(5)]
# [0, 1, 2, 3, 4]
l1 = [1,2,3,4]
result =[ x*2 for x in l1]
print(result)

# 多个值
# [ '%s = %s' for (k, v) in a_map.items()]
l1 = [1,2,3,4]
l2 = [1,2,3,4]
double = [x+y for x in l1 for y in l2]
print(double)
# [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]

# 可以调用函数
# [ func(x) for x in l1]  #等价于map

# 条件列表解析
dp = [ x for x in range(100) if x%2 ==0 ]
print(dp)

# 嵌套列表解析
mat = [ [1, 2, 3],[4, 5, 6], [7, 8, 9]]

# 交换行列
[ [row[i] for row in mat] for i in (0,1,2)]

#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

'''
其他：
1.根据索引取元素时，需要进行边界检查 IndexError 切片取，不需要，超过边界不会异常
2.在迭代中修改列表 注意，不安全，不建议这么干但是可以 for i in l1[:]: l1.insert()......
3.多个list合成一个就是
['a','b',.....],['a','b'.....]['a','b'.....]
变为 ['a','b',.....,'a','b'.....'a','b'.....]
'''
sum ([[ 'a', 'b' ],['a' , 'b'],[ 'a' ,'b' ]], [])
# ['a' , 'b' , 'a', 'b' , 'a' , 'b']
list (itertools .chain([ 'a' ,'b' ],[ 'a', 'b' ],['a' , 'b']))
# ['a' , 'b' , 'a', 'b' , 'a' , 'b']