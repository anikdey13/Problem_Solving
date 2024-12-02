
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print("Special")
    else:
        for i in range(2,22):
            if i ** 6 == n:
                print("Special")
                break
        else:
            print("Ordinary")