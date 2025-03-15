from collections import defaultdict, deque

def solve_plate_order(statements):
    # Graph representation
    graph = defaultdict(list)
    in_degree = {plate: 0 for plate in "ABCDE"}
    
    # Build the graph
    for statement in statements:
        if statement[1] == '>':
            larger, smaller = statement[0], statement[2]
        else:  # '<'
            larger, smaller = statement[2], statement[0]
        
        graph[larger].append(smaller)
        in_degree[smaller] += 1
    
    # Perform topological sorting using Kahn's algorithm
    queue = deque([plate for plate in "ABCDE" if in_degree[plate] == 0])
    order = []
    
    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for contradictions (cycle detection)
    if len(order) != 5:
        return "impossible"
    
    return ''.join(order)

# Example usage:
statements = []
for _ in range(6):
    statements.append(input())

print(solve_plate_order(statements))
