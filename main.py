from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Run matches
print("Quincy Match:")
play(player, quincy, 1000)

print("\nAbbey Match:")
play(player, abbey, 1000)

print("\nKris Match:")
play(player, kris, 1000)

print("\nMrugesh Match:")
play(player, mrugesh, 1000)

# Uncomment below to run tests
from test_module import test_player
test_player(player)
