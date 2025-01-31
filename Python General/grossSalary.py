basicSalary = int(input("Enter Basic salary = "))
HRA = 0
DA = 0
if basicSalary < 10000:
    HRA = basicSalary *(67/100)
    DA = basicSalary * (73/100)
elif basicSalary >=10000 and basicSalary <= 20000:
    HRA = basicSalary * (69 / 100)
    DA = basicSalary * (76/ 100)
else:
    HRA = basicSalary * (73 / 100)
    DA = basicSalary * (89 / 100)
GrossSalary = HRA+DA+basicSalary
print(f"Total Gross Salary = {GrossSalary}")
