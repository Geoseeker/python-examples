from employee import Employee

class HourlyEmployee(Employee):

    def computePayment(self, hours):
        return hours * self.getSalary()
