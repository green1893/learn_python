# if语法结构
cars = ['bmw','audi','honda','toyota']
for car in cars:
    if car == 'honda':
        print("Do You Like " + car.upper() + "?")
    else:
        print(car.title())
print("Complete!\n")

# and关键字
names = ["zhangsan","lisi","WangWu"]
age = 20
for name in names:
    if name.lower() == 'wangwu' and age <= 20:
        print(name + "，你就是我要找的人")
print("寻人结束\n")

# 数组值快速查找
if 'lisi' in names:
    print("你肯定能找到李四\n")

# elif
age = 18
if age < 4:
    print("门票全免")
elif age < 18:
    print("门票8折")
else:
    print("全票")

# 空列表判断
topics = []
# 不成立
if topics:
    print("empty array")
else:
    print("Haha")

# 通过长度检查，成立
if len(topics) == 0:
    print("Got it")
# 语法判断，成立
if topics is not None:
    print("Got it either")
