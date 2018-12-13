from random import randint
from time import sleep

guess = int(raw_input("What's your guess?"))


def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is %d" % max_val
  if guess > max_val:
    print "Too high of a guess!"
    roll_dice
  else:
    print "Rolling..."
    sleep(2)
    print "%d" % (first_roll)
    sleep(1)
    print "%d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if total_roll == guess:
      print "You've won!"
    elif total_roll != guess:
      print "You've lost..."

roll_dice(6)
