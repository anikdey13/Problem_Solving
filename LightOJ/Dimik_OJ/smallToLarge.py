t = int(input())
for i in range(t):
    n = input()
    k = ' '.join(sorted(n.split(" "), key=int))
    print(f"Case {i+1}: {k}")