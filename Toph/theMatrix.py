#Problem link
# https://toph.co/p/the-matrix

for _ in range(int(input())):
    n = int(input())
    numOfRectangle = int(((n * (n + 1)) / 2) ** 2)
    numOfSquare = int(((n * (n + 1) * ((2 * n) + 1)) / 6))
    print(f"{1 - (numOfSquare /numOfRectangle):.6f}")