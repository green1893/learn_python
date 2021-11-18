# 数组排序
cars = ['bmw','audi','honda','toyota']
cars.sort()
print(cars)

# 首字母反序排列
cars.sort(reverse=True)
print(cars)

print('***********')

# 排序但不影响原数组
print(sorted(cars))
print(cars)

# 数组元素反序
cars = ['bmw','audi','honda','toyota']
cars.reverse()
print(cars)

# 数组长度
print(len(cars))

# 数据类型混合
cars.append(1);
print(cars)
print(str(cars[-1]) + " is a car brand?")