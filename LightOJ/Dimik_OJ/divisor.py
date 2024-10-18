t = int(input())

for i in range(t):
    n = int(input())
    print(f"Case {i+1}: ", end="")
    for j in range(1,n+1):
        if n % j == 0:
            print(j, end=" ")
    print()