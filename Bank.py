#ABC


print("========WELCOME TO SBI BANK==========")
pinNumber = int(input("Enter Pin Number  = "))
def Validation():
    correctPin = 1234
    if correctPin == pinNumber:
        process()
    else :
        print("Invalid Pin Number")

def viewOptions () :
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Bal Enquiry")
    print("0.Exit")
    operation = int(input("enter operation = "))

    match operation:
        case 1:
            print("1st")
        case 2:
            print("1st")

        case 3:
            print("1st")

        case 0:
            print("1st")

Validation()