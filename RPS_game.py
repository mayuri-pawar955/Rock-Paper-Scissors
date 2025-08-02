import random

def play(player1, player2, num_games=100):
    p1_score = 0
    p2_score = 0
    p1_prev = ""
    p2_prev = ""
    for _ in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if p1_move == p2_move:
            pass
        elif p1_move == 'R' and p2_move == 'S':
            p1_score += 1
        elif p1_move == 'P' and p2_move == 'R':
            p1_score += 1
        elif p1_move == 'S' and p2_move == 'P':
            p1_score += 1
        else:
            p2_score += 1

        p1_prev = p1_move
        p2_prev = p2_move

    print(f"Final Score:\nPlayer 1: {p1_score}\nPlayer 2: {p2_score}")

def quincy(prev_play):
    return "P"

def abbey(prev_play, counter=[0]):
    options = ["R", "R", "P", "P", "S"]
    choice = options[counter[0] % len(options)]
    counter[0] += 1
    return choice

def kris(prev_play):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) >= 3:
        last_three = "".join(opponent_history[-3:])
        if last_three == "RRR":
            guess = "P"
        elif last_three == "PPP":
            guess = "S"
        elif last_three == "SSS":
            guess = "R"
    return guess
