# Operators
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership operators
# 7. Bitwise Operators


# a= 10
# b= 20

# # Arithmetic Operators
# add = a+b
# sub = a-b
# mul = a*b
# div = a/b
# mod = a%b
# exp = a**b
# floor_div = a//b

# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)
# print(exp)
# print(floor_div)


# Assignment Operator

# a= 10
# b= 20
# x +=3 --> x = x+3
# -=
# *=
# /=
# %=
# ^= or **=
# >>= --> x = x>>3
# <<= --> x = x<<3
# //=

# a += 3
# print(a)

# a = x**3
# 1010 xor 0011
# print(a)

# x = x>>3
# print(x)


# a= 10
# b= 10
# print(a == b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)


# num = int(input)


# # Input from the user
# num = int(input("Enter a number: "))

# # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "not prime")
#             break
#     else:
#         print(num, "is prime")
# else:
#     print(num, "not prime")


# # Find the element in the array with O(logN) Time complexity .
# # I/P: arr = [6, 7, 8, 10, 19]

# # Find k = 19
# # OP: 4


# arr = [6, 7, 8, 10, 19]
# val = 19

# i = 0
# for i in range(0, len(arr)):
#     if arr[i] == val:
#         print(i)
#     else:
#         pass

# #OR for more readability

# arr = [6, 7, 8, 10, 19]
# val = 19

# if val in arr:
#     print(arr.index(val))
# else:
#     print("val not in arr")

# #logical Operators
# x = 15
# ans = x<10 and x<20
# print(not(ans))
# # returns true when both conditions are satisfied

# ans = x<10 or x<20
# print(not(ans))
# #returns true when even one condition is satisfied


# # Membership operator
# x = [1, 2, 3, 4, 5]
# print(4 not in x)
# print(4 in x)

# # identity operators
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
# z = x
# print(x is not z)
# print(x == y)


##Bitwise operators
# &
# |
# ~
# ^