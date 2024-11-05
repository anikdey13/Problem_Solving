for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    count = 0
    for i in range(a,b):
        isprime = False
        for j in range(2,int(i/2)):
            if i % j == 0:
                isprime = True
        if isprime:
            count+=1
    print(count)