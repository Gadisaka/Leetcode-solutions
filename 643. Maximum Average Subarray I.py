nums = [2,2,3,2]
k = 2


def func(nums , k):
    max_avg = -10000000
    sum = 0
    start = 0

    while start < len(nums) - k + 1:
        for i in range(start , start + k , 1):
            sum += nums[i]
        avg = sum / k
        max_avg = max(max_avg , avg)
        start += 1

    return max_avg


print(func(nums , k ))