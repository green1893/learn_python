"""读取文件获取数据"""
with open("data/auther_names.txt") as file_object:
    content = file_object.read()
    print(content + "\n")

with open("data/auther_names.txt") as file_object:
    for name in file_object:
        print(name.rstrip())