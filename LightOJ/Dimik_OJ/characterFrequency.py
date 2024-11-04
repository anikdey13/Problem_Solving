t = int(input())

for _ in range(t):
    sentence = input()
    char = input()
    if char in sentence:
        freq = sentence.count(char)
        print(f"Occurrence of '{char}' in '{sentence}' = {freq}")
    else:
        print(f"'{char}' is not present")
