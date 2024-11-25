for _ in range(int(input())):
    n, S = map(int, input().split())
    A = list(map(int, input().split()))

    

    def check(A , S):
        myJ = 0
        myList = []
        low = 0 
        high = S - 1
        while low <= high:
            mid = (low + high) // 2
            if mid != 0:
                for val in A:
                    myList.append(val // mid)
                if sum(myList) == S:
                    myJ = mid
                    break
                elif sum(myList) < S:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                return 0
        return myJ

    result = check(A, S)
    if result == 0:
        print("-1")
    else:
        print(result)



# for _ in range(int(input())):
#     n, S = map(int, input().split())
#     A = list(map(int, input().split()))
#     maxA = max(A)

#     myJ = 0

#     for j in range(1, maxA + 1):
#         myList = []
#         for aVal in A:
#             myList.append(aVal // j)

#         if sum(myList) == S:
#             myJ = j
#     if myJ != 0:
#         print(myJ)
#     else:
#         print("-1")