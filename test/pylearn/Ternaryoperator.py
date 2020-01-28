
# 伪代码
#如果条件为真，返回真 否则返回假
# condition_is_true if condition else condition_is_false

is_fat = True
state = "fat" if is_fat else "not fat"
print(state)

# 伪代码:
# #(返回假，返回真)[真或假]
# (if_test_is_false, if_test_is_true)[test]

fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
#输出: Ali is fat

condition = True
print(2 if condition else 1/0)
#输出: 2
print((1/0, 2)[condition])

