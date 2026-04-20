import numpy as np

states = [(0,0), (0,1), (1,0), (1,1)]
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
goal = (1,1)
trap = (1,0)

gamma = 0.9

def step(state, action):
    i, j = state
    if action == 'UP':
        i -= 1
    elif action == 'DOWN':
        i += 1
    elif action == 'LEFT':
        j -= 1
    elif action == 'RIGHT':
        j += 1
    i = max(0, min(i, 1))
    j = max(0, min(j, 1))
    return (i, j)

def reward(state):
    if state == goal:
        return 10
    if state == trap:
        return -5
    return -1

def policy_iteration():
    policy = {s: np.random.choice(actions) for s in states if s != goal}
    V = {s: 0.0 for s in states}

    while True:
        while True:
            delta = 0
            for s in states:
                if s == goal:
                    continue
                v = V[s]
                ns = step(s, policy[s])
                V[s] = reward(ns) + gamma * V[ns]
                delta = max(delta, abs(v - V[s]))
            if delta < 0.01:
                break

        stable = True
        for s in states:
            if s == goal:
                continue
            old = policy[s]
            policy[s] = max(
                actions,
                key=lambda a: reward(step(s, a)) + gamma * V[step(s, a)]
            )
            if old != policy[s]:
                stable = False

        if stable:
            break

    return policy, V

policy, V = policy_iteration()

print("Policy Iteration Results:")
for state, action in policy.items():
    print(f"State: {state}, Action: {action}, Value: {round(V[state], 2)}")
