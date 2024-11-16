
nums = [20,100,10,12,5,13]

def fun(nums):
    n1 , n2 = sys.maxsize , sys.maxsize

    for n in nums:
        if n > n2:
            return True 
        if n <= n1:
            n1 = n
        elif n <= n2:
            n2 = n
    return False  