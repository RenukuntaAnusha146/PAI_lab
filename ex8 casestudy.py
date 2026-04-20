states = [0, 1, 2]
actions = [0, 1]
gamma = 0.9

def reward(state, action, demand):
    stock = min(state + action, 2)
    if demand > stock:
        return -5
    return 10 * demand - stock

def next_state(state, action, demand):
    stock = min(state + action, 2)
    return max(0, stock - demand)

def value_iteration():
    V = {s: 0.0 for s in states}
    while True:
        delta = 0
        for s in states:
            v = V[s]
            V[s] = max(
                sum(0.5 * (reward(s, a, d) + gamma * V[next_state(s, a, d)])
                    for d in [0, 1])
                for a in actions
            )
            delta = max(delta, abs(v - V[s]))
        if delta < 0.01:
            break
    return V

V = value_iteration()

print("Value Iteration Results:")
for state, value in V.items():
    print(f"State: {state}, Value: {round(value, 2)}")
