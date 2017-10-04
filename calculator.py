"""
Module that implements simple arithmetic operations
"""

def add(arg1, arg2):
    
    if float(arg1) != arg1 or float(arg2) != arg2:
        raise Exception("Provided arguments not numerical!")

    return arg1 + arg2 

def multiply(arg1, arg2):
     
    if float(arg1) != arg1 or float(arg2) != arg2:
        raise Exception("Provided arguments not numerical!")

    return arg1 * arg2 


