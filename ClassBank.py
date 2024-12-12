class Bank:
    totalBalance=0
    def viewOptions(self):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Bal Enquiry")
        print("0.Exit")
        operation = int(input("enter operation = "))

        match operation:
            case 1:
                depositAmount = int(input("Enter the Amount to be Deposited = "))
                self.totalBalance = self.totalBalance+depositAmount
            case 2:
                withdrawAmount = int(input("Enter The Withdraw Amount"))
                self.totalBalance = self.totalBalance - withdrawAmount
            case 3:
                print(f"Total Amount In the Account is = {self.totalBalance}")

            case 0:
                exit()

    def Validation(self):
        correctPin = 1234
        for i in range (1,4):
            pinNumber = int(input("Enter Pin Number  = "))
            if correctPin == pinNumber:
                obj.viewOptions()
                exit()
            else:
                print("Enter  Pin Number once")
        if pinNumber != correctPin:
            print("out of ATM")




obj = Bank()
obj.Validation()