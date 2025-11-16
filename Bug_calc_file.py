def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def power(num1, num2):
    #buggy code - returns multiplication instead of raising to power
    return num1 * num2

def average(nums):
    #buggy code - total is not declared
    for num in nums:
        total += num
    return total / len(nums)