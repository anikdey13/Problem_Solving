for i in range(int(input())):
    s = input().lower()
    if len(s) > 10:
        print(s[0] + str(len(s) - 2) + s[len(s) - 1])
    else:
        print(s)