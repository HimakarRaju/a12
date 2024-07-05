# Document: Design of Two Modular Functions

## Introduction

Modularity is a way of making a program easier to handle. 
It splits a program into smaller parts called modules or functions. 
Each function does a specific job. This makes the code neat, easy to read, easy to test, and easy to maintain. 

#### In this we will talk about how to design two functions:

1. find the factorial of a number, and
2. find a specific Fibonacci number.

We'll also include their pseudocode
Explain how modularity can improve code reuse and similarities.

### Function 1: Factorial of a Number

The factorial of a positive integer n is the product of all positive integers less than or equal to n. 
It is denoted by n!

For example, 6 != 6x5x4x3x2x1 = 720. 
The factorial of 0 is defined to be 1.

### Pseudocode

```python
Function factorial(n: Integer) → Integer:
    If n < 0:
Return - 1  Negative number error case
   Else If n == 0:
        Return 1
    Else:
        result = 1
        For i from 1 to n:
result = result * i
       End For
        Return result
End Function
```

#### Explanation

1. Input Validation: The function tidies up the input n to ensure it's a nonnegative number.
2. Starting Point: If n is 0, the function gives back 1.
3. Calculation: If n is a positive number, the function begins with a result of 1 and multiplies it by every number from 1 to n.
4. ** Final Result**: In the end, it gives back the calculated value.

### Function 2: nth Fibonacci Number

The Fibonacci sequence is a list of numbers where each number is the sum of the two before it. We start with numbers 0 and 1. The nth Fibonacci number is represented as F(n). For example, the sequence starts like this: 0, 1, 1, 2, 3, 5, 8, ….

```python
Pseudocode

Function fibonacci(n: Integer) → Integer:
    If n < 0:
Return - 1  Negative integer case
   Elif n == 0:
        Return 0
    Elif n == 1:
        Return 1
    Else:
        a = 0
b = 1
       For i from 2 to n:
            temp = a + b
            a = b
            b = temp
End For
       Return b
End Function

```

#### Explanation

1. Check Input: The function checks if the input n is a positive number or zero.
2. Starting Points: If n is 0, the function gives back 0. If n is 1, it gives back 1.
3. Making Calculations: If n is more than 1, the program keeps the last two Fibonacci numbers in two local variables:  a & b. The program then keeps updating these two variables to work out the n-th Fibonacci number.
4. Give the Result: The function gives back the n-th Fibonacci number, which is kept in b.

#### Advantages of using modules in programming

1. Reuse of Code : You can use a module function in different programs or different parts of the same program. This cuts down on repeating code.
2. Easier to Maintain: Splitting a program into smaller functions helps find and fix mistakes more easily.
3. Easier to Read: Modules make code easier to read because each function does a clear, specific task.
4. Testing: You can test each module separately to make sure every part of the program works right.
5. Teamwork: With modules, different developers can work on different functions at the same time. This makes development faster.

## Conclusion

Creating small, separate functions to calculate things like a number's factorial or the nth Fibonacci number shows that dividing tasks into smaller parts improves how we can reuse and organize code. By following this method, coders can make their code more efficient, easier to keep up, and simpler to understand.
