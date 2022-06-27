# April Laird
# 03/28/21
# Laird_Employee.py
# Module contains Employee and ProductionWorker classes


# Create Employee superclass
class Employee:
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num

    # Getters and setters
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_num(self):
        return self.__emp_num


# Create ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_num, shift, pay):
        # Call the superclass
        Employee.__init__(self, emp_name, emp_num)
        self.__shift = shift
        self.__pay = pay

    # Getters and setters
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        # if statement changes input to either day or night
        if self.__shift == '1':
            self.__shift = 'Day'
        else:
            self.__shift = 'Night'
        return self.__shift

    def get_pay(self):
        return self.__pay
