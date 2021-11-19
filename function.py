# def greet_user():
#     """显示最简单的问候语"""
#     print("Hello! everyone!")

# def greet_user(name):
#     print("Hello," + name + "! Nice to meet you.")

# greet_user("Zhansan")


def describe_pet(animal_type, pet_name="anonymity"):
    print("\nI have a " + animal_type + ".")
    print("Pet name is " + pet_name.title())

describe_pet("cat","Tom")

# 关键字实参调用方式，顺序不重要
describe_pet(pet_name="Jim", animal_type="dog")

# 形参默认值，pet_name参数
describe_pet("hourse")

# 函数返回值
def get_formatted_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()
name = get_formatted_name('zhiwu',"zhao")
print(name)

# 非定长入参
def make_pizza(*toppings):
    print(toppings)
make_pizza("one")
make_pizza("second","third","four")