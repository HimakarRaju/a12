# mylist = ["debjyothi","Meghana","Gopi","Dhanashree"]

# for i in mylist:
#     print(i)

# for i in range(10):
#     print(i)

# #while loop
# x = 0
# while x<10:
#     print(x)

x = int(input("Enter the number : "))
for i in range(1, 11):
    result = x * i
    print(f'{x} multiply by {i} = {result}')







def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial())