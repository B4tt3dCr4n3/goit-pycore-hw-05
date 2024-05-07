'''
Task 2. Write a function that extracts all numbers from a given text and 
sums them to calculate the total income.
'''

import re
from typing import Callable

def generator_numbers(text: str):
    '''
    Generator function that extracts all numbers from a given text.
    '''
    pattern = r'\b[-+]?[0-9]*\.?[0-9]+\b' # Regular expression pattern to match numbers
    for match in re.findall(pattern, text): # Find all matches in the text
        yield float(match.strip()) # Yield the number

def sum_profit(text: str, func: Callable):
    '''
    Function that sums all numbers extracted from a given text.
    '''
    total_profit = 0 # Variable to store the total profit
    for number in func(text): # Iterate over the numbers extracted from the text
        total_profit += number # Sum the numbers
    return total_profit # Return the total profit

# Test the function
TEXT = '''The employee's total income consists of several parts: 1000.01
as the main income, supplemented by additional income of 27.45 and 324.00 USD.'''

total_income = sum_profit(TEXT, generator_numbers) # Sum all numbers in the text

print(f"Total income: {total_income}") # Total income: 1351.46
