name = input("What's your name?\n")
print("Hello," + name + "! \n")

# while and break
idx = 0
while idx <= 5:
    print("current index is " + str(idx))
    if (idx / 2) > 1:
        break
    idx += 1