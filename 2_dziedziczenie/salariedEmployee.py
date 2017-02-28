from employee import Employee

class SalariedEmployee(Employee):

    def computePayment(self):
        return 190 * self.getSalary()
