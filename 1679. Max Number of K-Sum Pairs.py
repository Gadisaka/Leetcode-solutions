# 1679. Max Number of K-Sum Pairs

nums = [1,2,3,4]  
k = 5

def maxOperations(nums , k):
    from collections import Counter
    count = 0
    nums = Counter(nums)
    for num in nums:
        if k - num in nums:
            count += min(nums[num] , nums[k - num])
    return count // 2

print(maxOperations(nums , k))
