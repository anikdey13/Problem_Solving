for i in range(1 ,int(input()) + 1):
    n = int(input())
    queue = list(map(int,input().split()))

    for t, (n, heights) in enumerate(queue,1):
        # Precompute maxLeft and minRight
        maxLeft = [-float('inf')] * n
        minRight = [float('inf')] * n
    print(maxLeft)
    print(minRight)









# def solve(test_cases):
#     results = []
#     for t, (N, heights) in enumerate(test_cases, 1):
#         # Precompute maxLeft and minRight
#         maxLeft = [-float('inf')] * N
#         minRight = [float('inf')] * N
        
#         for i in range(1, N):
#             maxLeft[i] = max(maxLeft[i - 1], heights[i - 1])
        
#         for i in range(N - 2, -1, -1):
#             minRight[i] = min(minRight[i + 1], heights[i + 1])
        
#         # Find the candidate
#         found = False
#         for i in range(N):
#             if heights[i] > maxLeft[i] and heights[i] < minRight[i]:
#                 results.append(f"Case {t}: {i + 1}")
#                 found = True
#                 break
        
#         if not found:
#             results.append(f"Case {t}: Humanity is doomed!")
    
#     return "\n".join(results)

# # Input
# T = int(input())
# test_cases = []
# for _ in range(T):
#     N = int(input())
#     heights = list(map(int, input().split()))
#     test_cases.append((N, heights))

# # Solve and Output
# print(solve(test_cases))


