from Game import Game


g1 = Game("Chess", 2, "Board")
print("Using __str__():", g1)
print("Using __format__():", f"{g1}")
print("Using __repr__():", [g1])