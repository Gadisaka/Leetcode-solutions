nums = [-1,1,0,-3,3]

ans = []
for i in range(len(nums)):
    temp = 1
    for j in range(len(nums)):
        if j == i:
            continue
        else:
            temp *= nums[j]
    ans.append(temp)
print(ans)