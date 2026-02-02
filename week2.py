from collections import deque

def bfs(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    path = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == target:
            result = []
            while (x, y) != (0, 0):
                result.append((x, y))
                x, y = path[(x, y)]
            result.append((0, 0))
            result.reverse()
            return result

        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)
                path[state] = (x, y)

    return None


jug1 = 4
jug2 = 3
target = 2

solution = bfs(jug1, jug2, target)
print("Path:")
for step in solution:
    print(step)
