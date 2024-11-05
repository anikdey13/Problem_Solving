# for _ in range(int(input())):
#     n = int(input())
#     sum = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum+=i
#     if n == sum:
#         print(f"YES, {n} is a perfect number!")
#     else:
#         print(f"NO, {n} is not a perfect number!")

for _ in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            sum+=i
    if n == sum:
        print(f"YES, {n} is a perfect number!")
    else:
        print(f"NO, {n} is not a perfect number!")