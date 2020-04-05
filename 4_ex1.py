from sys import argv

rate, hours, bonus = argv
salary=int(rate)*int(hours)+int(bonus)
print("Salary is: ", salary)
