for i in range(int(input())):
    k = float(input())
    aspr = ((k**2 - 1) / (4 - k**2))**0.5
    print(f"Case {i+1}: {aspr:.4f}")
