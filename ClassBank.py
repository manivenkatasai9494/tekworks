class Bank:
    totalBalance = 0
    transaction = 0
    withdrawCount = 0  

    def Deposit(self):
        depositAmount = int(input("Enter the Amount to be Deposited = "))
        if depositAmount >= 100 and (depositAmount % 100) == 0 and depositAmount <= 50000:
            self.totalBalance = self.totalBalance + depositAmount

        if depositAmount < 100:
            print("You Have Entered less than RS.100")
        if (depositAmount % 100) != 0:
            print("The amount is not multiples of 100")
        if depositAmount > 50000:
            print("You have Entered more than 50k")
        obj.viewOptions()

    def Withdraw(self):
        if self.withdrawCount >= 3:
            print("You have reached the maximum withdrawal limit of 3.")
            obj.viewOptions()
            return

        withdrawAmount = int(input("Enter the withdraw Amount = "))
        if withdrawAmount > 100 and (withdrawAmount % 100) == 0 and withdrawAmount <= self.totalBalance and self.totalBalance >= 500 and withdrawAmount <= 20000:
            self.totalBalance = self.totalBalance - withdrawAmount
            self.withdrawCount += 1  
            self.transaction += 1  
            print(f"Withdrawal successful  new balance is {self.totalBalance}")
        else:
            if withdrawAmount < 100:
                print("withdrawAmount should be greater than 100")
            if (withdrawAmount % 100) != 0:
                print("The withdrawal amount was not multiples of 100")
            if withdrawAmount > self.totalBalance:
                print("Withdrawal money was greater than total balance")
            if self.totalBalance <= 500:
                print("Total Balance was Less Than RS.500")
            if withdrawAmount >= 20000:
                print("Withdrawal amount was greater than 20000")

        obj.viewOptions()

    def displayTotalBalance(self):
        print("Total Amount In the Account is =", self.totalBalance)
        obj.viewOptions()

    def viewOptions(self):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Bal Enquiry")
        print("0.Exit")
        operation = int(input("enter operation = "))
        while True:
            match operation:
                case 1:
                    self.Deposit()
                case 2:
                    self.Withdraw()
                case 3:
                    self.displayTotalBalance()
                case 0:
                    exit()
                case _:
                    print("Invalid choice  try again.")
                    operation = int(input("Enter operation = "))

    def Validation(self):
        correctPin = 1234
        for i in range(1, 4):
            pinNumber = int(input("Enter Pin Number = "))
            if correctPin == pinNumber:
                obj.viewOptions()
                exit()
            else:
                print("Enter Pin Number once more")
        if pinNumber != correctPin:
            print("Out of ATM")

obj = Bank()
obj.Validation()
