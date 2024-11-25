for _ in range(int(input())):
    word = input()
    for char in range(0, int(len(word)/2), 2):
        print(word[char], end="")
    print()