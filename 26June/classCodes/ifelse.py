num = int(input("Enter the number you want to check: "))

if num < 0:
    if num % 2 == 0:
        print("It is a negative even number")
    else:
        print("It is a negative odd number")
else:
    if num % 2 == 0:
        print("It is a positive even number")
    else:
        print("It is a positive odd number")
