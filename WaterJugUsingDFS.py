def dfs(state, jug1, jug2, target, visited, path):
    x, y = state

    if x == target:
        path.append(state)
        return True

    if state in visited:
        return False

    visited.add(state)
    path.append(state)

    states = [
        (jug1, y),
        (x, jug2),
        (0, y),
        (x, 0),
        (x - min(x, jug2 - y), y + min(x, jug2 - y)),
        (x + min(y, jug1 - x), y - min(y, jug1 - x))
    ]

    for s in states:
        if dfs(s, jug1, jug2, target, visited, path):
            return True

    path.pop()
    return False


jug1 = 4
jug2 = 3
target = 2

visited = set()
path = []

dfs((0, 0), jug1, jug2, target, visited, path)

print("Path:")
for step in path:
    print(step)
