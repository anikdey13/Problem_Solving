def subsets(nums):
    res = []  # To store all subsets

    subset = []  # Temporary list to store the current subset

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())  # Append a copy of the current subset to results
            return
        
        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)  # Start the DFS from the first index
    return res

# Example usage:
nums = [1, 2, 3]
print(subsets(nums))

