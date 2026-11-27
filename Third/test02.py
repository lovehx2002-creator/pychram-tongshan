bicycles = ['diming', 'xiaoniao', 'mojie']
print(bicycles)

# 添加元素到末尾
bicycles.append('xiaodao') # 已经改变了列表本身
print(bicycles)

bicycles.insert(1, 'haha')
print(bicycles)

# 删除元素
del bicycles[1]
print(bicycles)

# 删除元素，删除后可以使用
popnum = bicycles.pop(1)
print(popnum)
print(bicycles)

# 按照值来删除 remove
num1 = bicycles.remove('mojie')
print(bicycles)
print(num1)

