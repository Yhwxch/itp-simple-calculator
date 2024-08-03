import math
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Invalid value for denominator, can't divide by 0!"


def multiply(x, y):
    return x * y


def square(x):
    return x ** 2


def power(x, y):
    return x ** y


def sqrt(x):
    return math.sqrt(x)
