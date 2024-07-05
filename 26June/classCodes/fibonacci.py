#method1
def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(10))

# #method2
# n = 10  # Number of Fibonacci numbers to generate
# a = 0
# b = 1

# print(a)
# print(b)

# for _ in range(n - 2):
#     c = a + b
#     print(c)
#     a = b
#     b = c
