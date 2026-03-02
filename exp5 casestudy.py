# Alpha-Beta Pruning Implementation

# Example leaf node values (game outcomes)
game_scores = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, index, alpha, beta, is_maximizing):
    
    # Base case: If leaf node reached
    if depth == 0:
        return game_scores[index]

    if is_maximizing:
        max_eval = float('-inf')
        
        # Explore left and right child
        for i in range(2):
            eval = alphabeta(depth - 1, index * 2 + i, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            # Beta Cutoff
            if beta <= alpha:
                break
        
        return max_eval

    else:
        min_eval = float('inf')
        
        # Explore left and right child
        for i in range(2):
            eval = alphabeta(depth - 1, index * 2 + i, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            # Alpha Cutoff
            if beta <= alpha:
                break
        
        return min_eval


# Tree depth = 3 (8 leaf nodes)
depth = 3
result = alphabeta(depth, 0, float('-inf'), float('inf'), True)

print("Optimal Value using Alpha-Beta Pruning:", result)
