def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__ == "__main__":
    print(factorial(3))
    
'''
n = 0 --> 1
n >= 1 --> 1 + T(n-1)
'''