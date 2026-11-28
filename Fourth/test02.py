sum = 0

for value in range(1, 101):
    sum += value

print(sum)

print(type([1, 2, 3])) #是一个列表
print(type(range(1, 4))) #是一个range对象

num = list(range(1, 4))
print(num)
print(type(num))  # 通过list函数，将range对象转化为列表，有返回值

even_list = list(range(1, 11, 2))
print(even_list)

squares = [values ** 2 for values in range(1, 11)]
print(squares)
