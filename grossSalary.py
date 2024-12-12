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
#==================================================================================
basicSalary = int(input("Enter Basic Salary = "))
HRA, DA = (basicSalary * 0.67, basicSalary * 0.73) if basicSalary < 10000 else \
          (basicSalary * 0.69, basicSalary * 0.76) if basicSalary <= 20000 else \
          (basicSalary * 0.73, basicSalary * 0.89)
print(f"Total Gross Salary = {basicSalary + HRA + DA}")
