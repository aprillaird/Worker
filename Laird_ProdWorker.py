# April Laird
# 03/28/21
# Laird_ProdWorker.py
# Tracks employee info: name, emp#, shift, pay

import Laird_Employee


def main():
    # User inputs the information for the employee
    emp_name = input("Enter the employee's name: ")
    emp_num = input("Enter the employee number: ")
    shift = input("Enter the shift: 1 for day, 2 for night: ")
    pay = input("Enter the hourly pay rate: ")

    # Create a production worker object
    prod_worker = Laird_Employee.ProductionWorker(emp_name, emp_num, shift, pay)

    # Print the results using getters
    print("The employee's name is:", prod_worker.get_emp_name())
    print("The employee's number is:", prod_worker.get_emp_num())
    print("The employee's shift is:", prod_worker.get_shift())
    print("The employee's pay rate is: $", prod_worker.get_pay(), " per hour", sep='')


main()
