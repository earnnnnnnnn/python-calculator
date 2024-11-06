class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # Correct subtraction order: a - b
        return a - b

    def multiply(self, a, b):
        # Correct the loop to run exactly 'b' times instead of 'b+1'
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        # Adjust for negative multiplier
        if b < 0:
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = 0
        is_negative = (a < 0) != (b < 0)  # Determine if result should be negative
        a, b = abs(a), abs(b)
        
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        return -result if is_negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        
        is_negative = a < 0
        a, b = abs(a), abs(b)
        
        while a >= b:
            a = self.subtract(a, b)
        
        return -a if is_negative else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))            # Should print 3
    print("Example: subtraction: ", calc.subtract(4, 2))    # Should print 2
    print("Example: multiplication: ", calc.multiply(2, 3)) # Should print 6
    print("Example: division: ", calc.divide(10, 2))        # Should print 5
    print("Example: modulo: ", calc.modulo(10, 3))          # Should print 1