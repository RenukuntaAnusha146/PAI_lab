states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

start_prob = {'Rainy': 0.6, 'Sunny': 0.4}

transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

obs_sequence = ['walk', 'shop', 'clean']


def forward_algorithm():
    forward = []
    f0 = {}
    print("STEP 1: Initialization")
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][obs_sequence[0]]
        print(f"{state}: {start_prob[state]} * {emission_prob[state][obs_sequence[0]]} = {f0[state]}")
    forward.append(f0)
    for t in range(1, len(obs_sequence)):
        ft = {}
        print(f"\nSTEP {t+1}: Recursion for observation '{obs_sequence[t]}'")

        for curr_state in states:
            prob = 0
            for prev_state in states:
                val = (forward[t-1][prev_state] *
                       transition_prob[prev_state][curr_state])
                print(f"{prev_state} -> {curr_state}: {forward[t-1][prev_state]} * {transition_prob[prev_state][curr_state]} = {val}")
                prob += val

            ft[curr_state] = prob * emission_prob[curr_state][obs_sequence[t]]
            print(f"{curr_state} after emission: {prob} * {emission_prob[curr_state][obs_sequence[t]]} = {ft[curr_state]}")

        forward.append(ft)
    print("\nSTEP 4: Termination")
    total_prob = sum(forward[-1].values())
    print(f"Final Probability = {total_prob}")

    return total_prob


result = forward_algorithm()
