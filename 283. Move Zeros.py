# [1,0,0,0,10,0,0,12,56,87,545454,0,0,65,6,0,2,58,2,0,3]
nums = [4,2,4,0,0,3,0,5,1,0]

l = 0
r = 1

if 0 in nums:
    while r < len(nums):
        if nums[l] == 0:
            if nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r += 1
            else:
                r += 1
        else:
            l += 1
            r += 1


print(nums)