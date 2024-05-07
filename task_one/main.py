'''
Task 1. Write a function that calculates the n-th number in the Fibonacci 
sequence using a cache to store previously calculated values.
'''

def caching_fibonacci():
    '''
    Function that calculates the n-th number in the Fibonacci 
    sequence using a cache to store previously calculated values.
    '''
    cache = {} # Cache to store previously calculated values

    def fibonacci(n): # Function to calculate the n-th number in the Fibonacci sequence
        if n <= 0: # If n is less than or equal to 0, return 0
            return 0
        if n == 1: # If n is 1, return 1
            return 1
        if n in cache: # If n is in cache, return the value of n from cache
            return cache[n]
        result = fibonacci(n - 1) + fibonacci(n - 2) # Calculate the n-th number
        # in the Fibonacci sequence
        cache[n] = result # Store the value of n in cache
        return result # Return the value of n

    return fibonacci # Return the function fibonacci

# Test the function
fib = caching_fibonacci()

# Test cases
print(fib(10)) # 55
print(fib(15)) # 610
