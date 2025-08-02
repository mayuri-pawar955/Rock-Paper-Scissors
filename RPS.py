import random

def player(prev_play, opponent_history=[]):
    # Only track valid moves
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    guess = predict_opponent_move(opponent_history)

    return counter_move(guess)

def predict_opponent_move(history):
    patterns = {}
    for i in range(len(history) - 3):
        seq = tuple(history[i:i+3])
        next_move = history[i+3]
        if next_move not in ["R", "P", "S"]:
            continue  # Skip invalid moves

        if seq not in patterns:
            patterns[seq] = {"R": 0, "P": 0, "S": 0}
        patterns[seq][next_move] += 1

    last_seq = tuple(history[-3:])
    if last_seq in patterns:
        predicted = max(patterns[last_seq], key=patterns[last_seq].get)
    else:
        predicted = random.choice(["R", "P", "S"])

    return predicted

def counter_move(move):
    return {"R": "P", "P": "S", "S": "R"}[move]
