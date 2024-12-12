empSalary = int(input("Enter Employee Salary = "))
shoppingBill1 =int(input("Enter shoppingBill_1 Amount = "))
shoppingBill2 = int(input("Enter shoppingBill_2 Amount = "))
shoppingBill3 = int(input("Enter shoppingBill_3 Amount = "))
TotalAmtShoppingUsed = shoppingBill2+shoppingBill3+shoppingBill1
print(f"Total Amount used in Shopping is {TotalAmtShoppingUsed}")
print(f"Total percentage used in shopping = {(TotalAmtShoppingUsed/empSalary)*100}")

