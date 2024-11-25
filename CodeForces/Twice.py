# Kinich wakes up to the start of a new day. He turns on his phone, checks his mailbox, and finds a mysterious present. He decides to unbox the present.

# Kinich unboxes an array a
#  with n
#  integers. Initially, Kinich's score is 0
# . He will perform the following operation any number of times:

# Select two indices i
#  and j
#  (1≤i<j≤n)
#  such that neither i
#  nor j
#  has been chosen in any previous operation and ai=aj
# . Then, add 1
#  to his score.
# Output the maximum score Kinich can achieve after performing the aforementioned operation any number of times.

# Input
# The first line contains an integer t
#  (1≤t≤500
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (1≤n≤20
# ) — the length of a
# .

# The following line of each test case contains n
#  space-separated integers a1,a2,…,an
#  (1≤ai≤n
# ).

# Output
# For each test case, output the maximum score achievable on a new line.

# Example

# InputCopy
# 5
# 1
# 1
# 2
# 2 2
# 2
# 1 2
# 4
# 1 2 3 1
# 6
# 1 2 3 1 2 3

# OutputCopy
# 0
# 1
# 0
# 1
# 3

# Note
# In the first and third testcases, Kinich cannot perform any operations.

# In the second testcase, Kinich can perform one operation with i=1
#  and j=2
# .

# In the fourth testcase, Kinich can perform one operation with i=1
#  and j=4
# .


for i in range(int(input())):
    n = int(input())
    if len(n) >= 1 and len(n) <= 500:
        a = list(map(int, input().split()))
        if len(a) >= 1 and len(a) <= 20:
            for j in a:
                if j[] 
    else:
        print("Invalid Input")