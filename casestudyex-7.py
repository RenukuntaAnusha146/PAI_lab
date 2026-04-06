states = ['I', 'N', 'D']
obs = ['H', 'M', 'L']  # example sequence

start_prob = {'I': 0.5, 'N': 0.3, 'D': 0.2}

transition = {
    'I': {'I': 0.6, 'N': 0.3, 'D': 0.1},
    'N': {'I': 0.2, 'N': 0.5, 'D': 0.3},
    'D': {'I': 0.1, 'N': 0.3, 'D': 0.6}
}

emission = {
    'I': {'H': 0.7, 'M': 0.2, 'L': 0.1},
    'N': {'H': 0.3, 'M': 0.4, 'L': 0.3},
    'D': {'H': 0.1, 'M': 0.3, 'L': 0.6}
}

def forward():
    alpha = []

    # Step 1
    print("STEP 1: Initialization")
    a0 = {}
    for s in states:
        a0[s] = start_prob[s] * emission[s][obs[0]]
        print(f"{s}: {start_prob[s]} * {emission[s][obs[0]]} = {a0[s]}")
    alpha.append(a0)

    # Step 2
    for t in range(1, len(obs)):
        at = {}
        print(f"\nSTEP {t+1}: Observation = {obs[t]}")

        for curr in states:
            total = 0
            for prev in states:
                val = alpha[t-1][prev] * transition[prev][curr]
                print(f"{prev}->{curr}: {alpha[t-1][prev]} * {transition[prev][curr]} = {val}")
                total += val

            at[curr] = total * emission[curr][obs[t]]
            print(f"{curr} after emission: {total} * {emission[curr][obs[t]]} = {at[curr]}")

        alpha.append(at)

    print("\nFinal Probabilities:", alpha[-1])
    print("Total Probability:", sum(alpha[-1].values()))

forward()
