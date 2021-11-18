aliens = {
    "color":"white", 
    "points": 20
}
print(aliens['color'])

# 增加键值
aliens['x'] = 1.2
aliens['y'] = 2.0
print(aliens)

# 删除键值
del aliens['color']
print(aliens)

# 字典遍历:items()
for key,value in aliens.items():
    print(key.upper() + ":" + str(value))

for key in aliens.keys():
    print(key.upper())

for value in aliens.values():
    print(value)