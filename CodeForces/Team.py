matrix = []
for i in range(int(input())):
    row = list(map(int, input().split()))
    matrix.append(row)
count = 0
for j in matrix:
    if sum(j) >= 2:
        count += 1


print(count)