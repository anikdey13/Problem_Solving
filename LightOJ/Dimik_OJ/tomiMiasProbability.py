from math import factorial
from collections import Counter

t = int(input())  # Number of test cases

for _ in range(t):
    n = input().split()  # Split sentence into words
    word_count = len(n)  # Count the total number of words
    freq = Counter(n)  # Get the frequency of each word using Counter from collections
    
    # Calculate the factorial of the total number of words
    result = factorial(word_count)
    
    # For each word that appears multiple times, divide by the factorial of its frequency
    for count in freq.values():
        if count > 1:
            result //= factorial(count)
    
    # Output the result as 1/n!
    print(f"1/{result}")



# from math import factorial

# t = int(input())

# for _ in range(t):
#     n = input().split(" ")
    # ori_length = len(n)
    # unique_length = (len(set(n)))
    # if ori_length > unique_length:
    #     z = unique_length - 1
    #     f = ori_length - z
    #     y = factorial(ori_length) / factorial(f)
    #     print(f"1/{y:.0f}")
    # else:
    #     x = factorial(ori_length)
    #     print(f"1/{x:.0f}")