# test_module.py

import random

def test_player(player):
    opponent_history = []
    prev_play = ""
    for i in range(1000):
        move = player(prev_play, opponent_history)
        if move not in ["R", "P", "S"]:
            raise ValueError(f"Invalid move at round {i}: {move}")
        opponent_move = random.choice(["R", "P", "S"])
        opponent_history.append(opponent_move)
        prev_play = opponent_move
    print("✅ Test passed: Your player made 1000 valid moves.")
