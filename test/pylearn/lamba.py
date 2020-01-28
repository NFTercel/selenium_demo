
# Map会将一个函数映射到一个输入列表的所有元素上
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

#列表函数
def multiply(x):
    return (x * x)
def add(x):
    return (x + x)
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# filter能创建一个列表，其中每个元素都是对一个函数能返回True
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
