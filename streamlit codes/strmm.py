import streamlit as st


class Bank:
    totalBalance = 0
    transaction = 0
    withdrawCount = 0

    def Deposit(self):
        depositAmount = st.number_input("Enter the Amount to be Deposited:", min_value=0, step=1, format="%d",
                                        key="depInput")
        if depositAmount >= 100 and (depositAmount % 100) == 0 and depositAmount <= 50000:
            self.totalBalance += depositAmount
            st.success(f"Deposited ₹{depositAmount}. New balance: ₹{self.totalBalance}.")
        else:
            if depositAmount < 100:
                st.error("You Have Entered less than ₹100.")
            if (depositAmount % 100) != 0:
                st.error("The amount is not in multiples of 100.")
            if depositAmount > 50000:
                st.error("You have Entered more than ₹50,000.")
        self.viewOptions()

    def Withdraw(self):
        if self.withdrawCount >= 3:
            st.error("You have reached the maximum withdrawal limit of 3.")
            self.viewOptions()
            return

        withdrawAmount = st.number_input("Enter the withdraw Amount:", min_value=0, step=1, format="%d",
                                         key="withdrawInput")
        if withdrawAmount >= 100 and (
                withdrawAmount % 100) == 0 and withdrawAmount <= self.totalBalance and self.totalBalance >= 500 and withdrawAmount <= 20000:
            self.totalBalance -= withdrawAmount
            self.withdrawCount += 1
            self.transaction += 1
            st.success(f"Withdrawal successful. New balance: ₹{self.totalBalance}.")
        else:
            if withdrawAmount < 100:
                st.error("Withdrawal amount should be greater than ₹100.")
            if (withdrawAmount % 100) != 0:
                st.error("The withdrawal amount is not in multiples of ₹100.")
            if withdrawAmount > self.totalBalance:
                st.error("Insufficient balance.")
            if self.totalBalance < 500:
                st.error("Minimum balance of ₹500 required.")
            if withdrawAmount > 20000:
                st.error("Maximum withdrawal limit is ₹20,000.")
        self.viewOptions()

    def displayTotalBalance(self):
        st.write(f"Total Amount In the Account: ₹{self.totalBalance}")
        self.viewOptions()

    def viewOptions(self):
        option = st.radio("Select an operation:", ["Deposit", "Withdraw", "Balance Enquiry", "Exit"], key="operation")
        if option == "Deposit":
            self.Deposit()
        elif option == "Withdraw":
            self.Withdraw()
        elif option == "Balance Enquiry":
            self.displayTotalBalance()
        elif option == "Exit":
            st.write("Thank you for using the ATM!")
            st.stop()

    def Validation(self):
        if "attempts" not in st.session_state:
            st.session_state.attempts = 3

        if st.session_state.attempts > 0:
            pinNumber = st.text_input("Enter PIN:", value="", max_chars=4, type="password", key="pin_input")

            if st.button("Submit PIN"):
                if pinNumber:  # Only process if input is not empty
                    try:
                        pinNumber = int(pinNumber)
                        if pinNumber == 1234:
                            st.success("PIN correct! Welcome.")
                            self.viewOptions()
                        else:
                            st.session_state.attempts -= 1
                            st.error(f"Incorrect PIN. You have {st.session_state.attempts} attempts remaining.")
                    except ValueError:
                        st.error("Please enter a valid numeric PIN.")
                else:
                    st.warning("Please enter your PIN.")
        else:
            st.error("You have exceeded the maximum number of attempts. Please leave the ATM.")
            st.stop()


# Instantiate the Bank class and start the program
obj = Bank()
obj.Validation()
