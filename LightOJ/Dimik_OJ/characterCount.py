from collections import Counter

for i in range (int(input())):
    s = input()
    count = Counter(s)
    for l in count:
        print(f"{l} = {count[l]}")