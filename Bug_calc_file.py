def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return None
    else:
        return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def power(num1, num2):
    return num1 ** num2

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

def num_range(nums):
    if not nums:
        return 0
    else:
        low = min(nums)
        high = max(nums)
        return high - low

#TODO add exponent