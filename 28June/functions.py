def add(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    result = b / a
    return result


num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

output1 = add(num1, num2)
output2 = sub(num1, num2)
output3 = mul(num1, num2)
output4 = div(num1, num2)

print(f'the addition of {num1} & {num2} is : {output1}')
print(f'the subtraction of {num1} & {num2} is : {output2}')
print(f'the multiplication of {num1} & {num2} is : {output3}')
print(f'the division of {num1} & {num2} is : {output4}')
