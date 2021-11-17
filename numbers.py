# range生成数组
for value in range(1,10):
    print(value)

numbers = list(range(1,5))
print(numbers)

# 指定步长,步长3
print(list(range(1,8,3)))

# 平方运算
squares = []
for num in range(1,10):
    squares.append(num**2)
print(squares)

# 一行缩写
squares = [value**2 for value in range(1,10)]
print(squares)

# 数组截取，从第3个开始到最后
print(squares[2:])