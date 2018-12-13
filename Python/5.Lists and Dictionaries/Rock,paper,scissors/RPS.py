from random import randint

option = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie": "Yawn it's a tie!", "won": "Yay you won!", "lost": "Aww you lost!"}

def decide_winner(user_choice, computer_choice):

  if  user_choice == computer_choice:
    print message["tie"]
  elif user_choice == option[0] and computer_choice == option[2]:
    print message["won"]
  elif user_choice == option[1] and computer_choice == option[0]:
    print message["won"]
  elif user_choice == option[2] and computer_choice == option[1]:
    print message["won"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = option[randint(0, 2)]
  print "user: " + user_choice
  print "computer: " + computer_choice
  decide_winner(user_choice, computer_choice)
play_RPS()

def x123():
  print 3

x123()
  