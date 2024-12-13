import streamlit as st
class Bank:
    totalBalance = 0
    transaction = 0
    withdrawCount = 0

    def Deposit(self):
        depositAmount = st.number_input("Enter the Amount to be Deposited = " , key="depInput")
        if depositAmount >= 100 and (depositAmount % 100) == 0 and depositAmount <= 50000:
            self.totalBalance = self.totalBalance + depositAmount

        if depositAmount < 100:
            st.write("You Have Entered less than RS.100")
        if (depositAmount % 100) != 0:
            st.write("The amount is not multiples of 100")
        if depositAmount > 50000:
            st.write("You have Entered more than 50k")
        obj.viewOptions()

    def Withdraw(self):
        if self.withdrawCount >= 3:
            st.write("You have reached the maximum withdrawal limit of 3.")
            obj.viewOptions()

        withdrawAmount = st.number_input("Enter the withdraw Amount = ", key="withDrawInput")
        if withdrawAmount > 100 and (withdrawAmount % 100) == 0 and withdrawAmount <= self.totalBalance and self.totalBalance >= 500 and withdrawAmount <= 20000:
            self.totalBalance = self.totalBalance - withdrawAmount
            self.withdrawCount += 1
            self.transaction += 1
            st.write(f"Withdrawal successful  new balance is {self.totalBalance}")
        else:
            if withdrawAmount < 100:
                st.write("withdrawAmount should be greater than 100")
            if (withdrawAmount % 100) != 0:
                st.write("The withdrawal amount was not multiples of 100")
            if withdrawAmount > self.totalBalance:
                st.write("Withdrawal money was greater than total balance")
            if self.totalBalance <= 500:
                st.write("Total Balance was Less Than RS.500")
            if withdrawAmount >= 20000:
                st.write("Withdrawal amount was greater than 20000")

        obj.viewOptions()

    def displayTotalBalance(self):
        st.write("Total Amount In the Account is =", self.totalBalance)
        obj.viewOptions()

    def viewOptions(self):
        st.write("1.Deposit")
        st.write("2.Withdraw")
        st.write("3.Bal Enquiry")
        st.write("0.Exit")
        operation = st.number_input("enter operation = ",key="operation_input1")
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
                    st.write("Invalid choice  try again.")
                    operation = st.number_input("Enter operation = ",key="operation_input2")

    def Validation(self):
        correctPin = 1234
        while True:
            for i in range(1, 4):
                pinNumber = st.number_input("Enter Pin Number:", min_value=1000, max_value=9999,key="pin_input")
                if correctPin == pinNumber:
                    obj.viewOptions()
                    exit()
                else:
                    st.write("Enter Pin Number once more")
            if pinNumber != correctPin:
                st.write("Out of ATM")

obj = Bank()
obj.Validation()



