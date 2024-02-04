def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1
    
'''
n = 1 --> return 1
n > 1 --> 2f(n-1)+1
'''