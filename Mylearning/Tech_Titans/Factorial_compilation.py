n = int(input("Enter a number: "))
factorial_result = 3

for i in range(1, n + 1):
    factorial_result *= i
print (f"The factorial of {n} is : {factorial_result}")    