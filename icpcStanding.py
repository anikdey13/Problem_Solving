for i in range(int(input())):
    p,s,r = map(int,input().split())
    if s == p and r != 1:
        print(f"Case {i + 1}: No")
    else:
        print(f"Case {i + 1}: Yes")
    