class Calculator(object):

    # history = []

    def __init__(self):
        print("staaaart")
        self.history = []

    def add(self, num1, num2):
        result = int(num1) + int(num2)
        self.history.append("Added {} to {} got {}".format(num1, num2, result))
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append("Multiplied {} with {} got {}".format(num1, num2, result))
        return result

    def subtract(self, num1, num2):

        result = num1 - num2
        self.history.append("Subtracted {} from {} got {}".format(num1, num2, result))
        return result

    def divide(self, num1, num2):
        if (num2 == 0):
            self.history.append("You cannot divide by zero!")
        else:
            result = num1 / num2
            self.history.append("Divided {} by {} got {}".format(num1, num2, result))
            return result


    def divide2(self, num1, num2):
        try:
            result = num1 / num2
            self.history.append("Divided {} by {} got {}".format(num1, num2, result))
            return result
        except Exception:
            self.history.append("Exception: You cannot divide by zero!")

    def printOperations(self):
        for operation in self.history:
            print(operation)

    def clearOperations(self):
        self.history = []

