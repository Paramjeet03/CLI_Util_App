class Math_util:
    def calculator(self, a, b, op):
        if op == "+":
            print( a + b)
        elif op == "-":
            print( a - b)
        elif op == "*":
            print( a * b)
        elif op == "/":
            print( "Cannot divide by zero" if b == 0 else a / b)
        else:
            print( "Invalid operator")

    def is_prime(self, n):
        if n <= 1:
            print("False")

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("False")



    def factorial(self, n):
        if n < 0:
            result = "❌ Factorial not defined for negative numbers."
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i

        print(f"Factorial of {n} is: {result}")

