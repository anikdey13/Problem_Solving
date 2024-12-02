x = 0
for _ in range(int(input())):
    exp = input()
    if exp == "++X" or exp == "X++":
        x+=1
    else:
        x-=1
print(x)