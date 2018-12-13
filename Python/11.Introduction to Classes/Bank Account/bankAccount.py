class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "%s's bank account: balance = $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "user's balance is $%.2f" % (self.balance)
  def deposit(self, amount):
    if amount <= 0:
      print "You need to enter an amount!"
      return
    else:
      print "You've deposited: $%.2f" % (amount)
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance :
      print "That's more than you have! lol"
      return
    else:
      print "You've withdrawn: $%.2f" % (amount)
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Jack")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
