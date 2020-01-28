# set(集合)是一个非常有用的数据结构。它与列表(list)的行为类似，区别在于set不能 包含重复的值。
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

l1 = [1,2,3,4]

[x for x in range(5)]
# [0, 1, 2, 3, 4]
l1 = [1,2,3,4]
[ x*2 for x in l1]
# [2, 4, 6, 8]

# 交集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

# 差集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))

a_set = {'red', 'blue', 'green'}
print(type(a_set))