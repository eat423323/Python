#View the calendar Add an event to the calendar Update an existing event Delete an existing event

from time import strftime, time

name = raw_input("What's your first name? ")
calender = {}

def welcome():
  print "Welcome! " + name
  print "the program is now running!"
  sleep(1)
  print strftime("%A %B %d, %Y")
  print strftime("%H:%M:%S")
  print "What would you like to do? "

def start_calender():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V" :
      if len(calender.keys()) < 1:
        print "Calender is empty!"
      else:
        print calender
    elif user_choice == "U":
      date = raw_input("What date?")
      update = raw_input("Enter the update: ")
      calender[date] = update
      print "Update successful!"
      print calender
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) >10 or int(date[6:] < int(strftime("%Y")):
        print "Invalid date"
        try_again = raw_input("Try again?")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calender[date] = event
        print calender
    elif user_choice == "D":
      if len(calender.key()) < 1:
        print: "calender is empty"
      else:
        event = raw_input("what event?")
        for date in calender.key():
          if event == calender[date]:
            del calender[date]
            print "successfully deleted!"
            print calender
        else:
          print "incorrect event!"
      elif ueser_choice == "X":
        start = False
      else:
        print "invalid command!"

start_calender()












        
