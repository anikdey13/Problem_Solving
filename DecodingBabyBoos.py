
def rep(a,b,s):
    for char in s:
        if char == b:
            s.replace(b,a)
            return s




for _ in range(int(input())):
    s = input()
    r = int(input())
    for _ in range(r):
        a , b = input().split()
        rep(a,b,s)
    print(s)