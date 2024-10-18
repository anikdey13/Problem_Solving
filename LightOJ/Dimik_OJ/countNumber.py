t = int(input())

for _ in range(t):
    n = input()
    k = n.strip().split(" ")
    count = len(k)
    for i in k:
        if i == "":
            count -= 1

    print(count)
    