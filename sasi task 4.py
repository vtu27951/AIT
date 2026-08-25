def minimax(depth, index, max_player, alpha, beta):
    if depth == 2:
        return scores[index]

    if max_player:
        best = -999

        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            False, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [6, 5, 8, 2]

result = minimax(0, 0, True, -999, 999)

print("Best attack score:", result)
