def isPowerOfTwo(n):
    x = 1
    while x < n :
        x *= 2
    return x == n 

print(isPowerOfTwo(7))