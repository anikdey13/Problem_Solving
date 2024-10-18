t = int(input())

for k in range(t):
    n = int(input())
    j = n * n
    for i in range(1,j+1):
        print("*", end="")
        if i%n==0:
            print()

    if k+1 != t: print()
    