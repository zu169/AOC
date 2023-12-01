import random

print("Welcome to Rock paper scissors")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
mode = int(input("choose a mode 1 player or 2 player "))
if mode == 1:
  p_choice = int(input("choose 1 rock, 2 paper,3 scissors "))
  choice = random.randint(1,3)
  if choice == 1:
    print("computer chooses rock")
  elif choice == 2:
    print("computer chooses paper")  
  elif choice == 3:
    print("computer chooses scissors")
  if p_choice == choice:
    print("its a draw")
  if p_choice == 1:
    choice == 2
    print("you lose")
  elif p_choice == 1:
    choice == 3
    print("you win")
  if p_choice == 2:
    choice == 1
    print("you win")
  elif p_choice == 2:
    choice == 3
    print("you lose")
  if p_choice == 3:
    choice == 1
    print("you lose")
  elif p_choice == 3:
    choice == 2
    print("you win")

if mode == 2:
  p_choice = int(input("player 1 choose 1 rock, 2 paper,3 scissors "))
  choice = int(input("player 2 choose 1 rock, 2 paper,3 scissors "))
  if choice == 1:
    print("player 2 chooses rock")
  elif choice == 2:
    print("player 2 chooses paper")  
  elif choice == 3:
    print("player 2 chooses scissors")
  if p_choice == choice:
    print("its a draw")
  if p_choice == 1:
    choice == 2
    print("p2 win")
  elif p_choice == 1:
    choice == 3
    print("p1 win")
  if p_choice == 2:
    choice == 1
    print("p2 win")
  elif p_choice == 2:
    choice == 3
    print("p2 win")
  if p_choice == 3:
    choice == 1
    print("p2 win")
  elif p_choice == 3:
    choice == 2
    print("p1 win")