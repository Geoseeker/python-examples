from calculator import Calculator


class AdvancedCalculator(Calculator):

    PI = 3.14159265

    def pow(self, num1, num2):
        result = pow(num1, num2)
        self.history.append("{}^{} got {}".format(num1, num2, result))
        return result

    def root(self, num1, num2):
        result = pow(num1, 1/num2)
        self.history.append("root {} of {} equals {}".format(num1, num2, result))
        return result

    @staticmethod
    def computeCircleRadius(r):
        return AdvancedCalculator.PI * pow(r, 2)





