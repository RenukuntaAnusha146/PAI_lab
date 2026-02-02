from collections import defaultdict

jug1, jug2, target = 4, 3, 2
visited = defaultdict(bool)

def waterJugSolver(x, y):
    if x == target:
        print(x, y)
        return True

    if visited[(x, y)]:
        return False

    visited[(x, y)] = True
    print(x, y)

    return (
        waterJugSolver(jug1, y) or
        waterJugSolver(x, jug2) or
        waterJugSolver(0, y) or
        waterJugSolver(x, 0) or
        waterJugSolver(x - min(x, jug2 - y), y + min(x, jug2 - y)) or
        waterJugSolver(x + min(y, jug1 - x), y - min(y, jug1 - x))
    )

print("Steps:")
waterJugSolver(0, 0)
