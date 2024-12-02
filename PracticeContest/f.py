for i in range(int(input())):
    d,m,y,ry = map(int, input().split())
    count = 0
    if m == 2 and d == 29:
        for j in range(y,ry+1,4):
            if j == y:
                continue
            if (j % 4 == 0 and j % 100 != 0) or j % 400 == 0:
                count+=1
    else:
        count = ry - y
    print(f"Case {i+1}: {count}")
