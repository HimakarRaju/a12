# 1. try - in this block well keep the code we want to execute
# 2. except - this is block helps to handle the error
# 3. else -  this block executes code if no error occurs
# 4. finally - it is always executed, no matter if we get any error or not

try:
    x = int(input("Enter a number : "))
    result = 10/x
except ValueError:
    print("You must give a number value")
except ZeroDivisionError:
    print("You cannot divide this number by zero")
else:
    print(f'The result is {result}')
finally:
    print("Execution is completed")
