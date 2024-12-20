# def CalculateBMI()
#     weight = float(input("enter your weight"))
#     height = float(input("enter your height"))
#     bmi = weight / height**2
#     print(bmi)
#     if bmi < 18.5:
#         print(f"You bmi is {bmi},you are under weight")
#     elif bmi < 25.5:
#         print(f"You bmi is {bmi},you are in normal weight")
#     elif bmi < 30:
#         print(f"You bmi is {bmi},you are over weight")
#     elif bmi < 35:
#         print(f"You bmi is {bmi},you are obese")
#     else:
#         print(f"You bmi is {bmi},you are clinically obese")

cart ={"Book":10000 ,"pen" :12000,"computer":18000}
total = 0
def CalculateTotal(cart):
    total = sum(cart.values())
    if total>=50000  :
        total = total - total*0.15
        return total
    elif total>10000 and total<20000 :
        total = total - total*0.10
        return total
    else :
        return total
print(CalculateTotal(cart))