# import math

# for _ in range(int(input())):
#     a,b = list(map(int,input().split()))

#     lcm = math.lcm(a,b)

#     print(f"LCM = {lcm}")

for i in range(int(input())):
    a,b = list(map(int,input().split()))

    if a > b:
        higher = a
    else:
        higher = b

    value = higher
    while True:
        if higher % a == 0 and higher % b == 0:
            print(f"LCM = {higher}")
            break
        else:
            higher+=value