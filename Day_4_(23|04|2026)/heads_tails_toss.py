import random

choosen_side = input("Heads or Tails?\n").strip().lower()
toss = random.randint(0,1)
if toss == 1 and choosen_side == "heads":
    print("you won!....its heads")
elif toss == 1 and choosen_side == "tails":
    print("you lost....its heads")
elif toss == 0 and choosen_side == "heads":
    print("you lost....its tails")
elif toss == 0 and choosen_side == "tails":
    print("you won!....its tails")
else:
    print("else statement")