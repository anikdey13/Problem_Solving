# num = int(input())
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i

# print(fact)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
