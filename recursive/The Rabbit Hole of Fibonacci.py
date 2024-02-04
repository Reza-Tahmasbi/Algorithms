def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
'''
n >= 3 --> f(n - 1) + f(n - 2)
f(1), f(2) = 1
'''