'''
这个案例并不是非常实用。生成器最佳应用场景是:你不想同一时间将所有计算出来的大
量结果集分配到内存当中，特别是结果集里还包含循环。
'''
# def generator_function():
#     for i in range(10):
#         yield i
# for item in generator_function():
#     print(item)

# 下面是一个计算斐波那契数列的生成器:
# generator version
# def fibon(n):
#     a=b=1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# for x in fibon(2):
#     print(x)



def generator_function():
    for i in range(3):
        yield i
gen = generator_function()
print('1: ',next(gen))
# Output: 0 print(next(gen))
# Output: 1
print('2: ',next(gen))
# Output: 2
print('3: ',next(gen))