#Problem C
# n = int(input())

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# Problem D
# a,b,c = map(int,input().split())

# myList = []
# for i in range(1,c+1):
#     if c % i == 0:
#         myList.append(i)

# count = 0
# for x in myList:
#     if x >= a and x <= b:
#         count += 1

# print(count)


#Problem E

# a,b = map(int,input().split())

# listA = []
# listB = []
# for i in range(1,a+1):
#     if a % i == 0:
#         listA.append(i)
# for j in range(1,b + 1):
#     if b % j == 0:
#         listB.append(j)

# common_elements = set(listA).intersection(listB)

# num = max(common_elements)

# print(num)


# n = int(input())

# inputList = list(map(int, input().split()))

# if len(inputList) != n:
#     print(f"Error: Expected {n} numbers, but got {len(inputList)}")
# else:
#     output = " ".join(map(str,inputList[::-1]))
#     print(output)


# n = int(input())

# inputList = list(map(int, input().split()))
# newlist = inputList[::-1]
# if len(inputList) != n:
#     print(f"Error: Expected {n} numbers, but got {len(inputList)}")
# elif inputList == newlist:
#     print("YES")
# else:
#     print("NO")

# n = input()

# if int(n[0]) % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")


# N = int(input())

# for i in range(1, N + 1):
#     spaces = ' ' * (N - i)
#     stars = ' '.join(['*'] * i)
#     print(spaces + stars)

# n = int(input())
# isPrime = True
# for i in range(2, int(n ** 0.5 + 1)):
#     if n % i == 0:
#         isPrime = False

# if isPrime:
#       print("NO PUNISHMENT")
# else:
#     for j in range(n):
#         print("I DID NOT DO THE ASSIGNMENT.")

# from collections import Counter

# s = input()

# freq = Counter(s)
# for i in sorted(freq):
#     print(f"{i} : {freq[i]}")

# exp = input().replace('/','//')
# print(eval(exp))


for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))

    if a/b == c/d:
        print("Equal")
    else:
        print("Not Equal")