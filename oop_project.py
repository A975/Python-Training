from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposite(500)

Dave.withdraw(10)
Dave.withdraw(10)

Dave.transfer(10, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAcc(1000,"Jim")

Jim.getBalance()

Jim.deposite(100)

Jim.transfer(100, Dave)
# Jim = InterestRewardsAcc(1000, "Jim")

# Jim.getBalance(100)

# Jim.transfer(100, Dave)

# Blaze = SavingsAcct(1000, "Blaze")

# Blaze.getBalance()

# Blaze.deposit(100)

# Blaze.transfer(10000, Sara)