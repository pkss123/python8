for i in range(4):
    for j in range(i):
        print(" ", end="")
    for k in range(4 - i):
        print("*", end="")
    print()
print()

for i in range(4):
    for j in range(4):
        if i <= j:
            print("*", end="")
        else :
            print(" ", end="")
    print()