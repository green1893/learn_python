# 数组
bicycles = ['永久','凤凰','dahon']
print(bicycles)
print(bicycles[1])
print(bicycles[2].title())

# 数组尾部特殊提取方法
print(bicycles[-1].title())
print("My fisrt bicycle was a " + bicycles[1].title() + ".")

# 数组值修改
moto = ["honda",'yamaha','suzuki']
moto[0] = 'ducati'
print(moto);

# 增加元素
moto.append('honda')
print(moto)

# 在指定位置插入元素
moto.insert(0, 'cf')
print(moto)

# 删除指定位置元素
del moto[1]
print(moto)

# 删除指定值元素
moto.remove("cf")
print(moto)