
import math
t = int(input())

for _ in range(t):
    n = int(input())
    k = str(math.factorial(n))
    j = ''.join(reversed(k))

    count = 0
    for i in j:
        if int(i) > 0:
            break
        else :
            count += 1

    print(count)


    
