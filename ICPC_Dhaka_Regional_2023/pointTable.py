for i in range(1,int(input()) + 1):
    a , b , c = map(int,input().split())
    sum = a + b + c
    if sum != 0 and sum <= 9:
        if sum < 6:
            print(f"Case {i}: invalidum")
        elif a == 6 and b == 1 and c==1:
            print(f"Case {i}: perfectus")
        elif a == 6 and b == 3 and c==0:
            print(f"Case {i}: perfectus")
        elif a == 3 and b == 3 and c==3:
            print(f"Case {i}: perfectus")
        elif a == 4 and b == 3 and c==1:
            print(f"Case {i}: perfectus")
        elif a == 2 and b == 2 and c==2:
            print(f"Case {i}: perfectus")
        elif a == 4 and b == 2 and c==1:
            print(f"Case {i}: perfectus")
        elif a == 4 and b == 4 and c==0:
            print(f"Case {i}: perfectus")
        else:
            print(f"Case {i}: invalidum")
    else:
        print(f"Case {i}: invalidum")