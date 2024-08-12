nums = [-4 , -2 , 1 , 4 , 8]
closest = nums[0]
for num in nums:
    if abs(num) < abs(closest):
        closest = num

if closest < 0 and abs(closest) in nums:
    ans =  abs(closest)
else:
    ans =  closest
print(ans)