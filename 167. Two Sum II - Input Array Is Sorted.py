numbers = [2,3,4]
target = 6
i , j = 0 , 0
left , right = 0 , len(numbers)  - 1
while(1):
    if numbers[left] + numbers[right] > target:
        right -= 1
    elif numbers[left] + numbers[right] < target:
        left += 1
    else:
        i , j = left + 1, right + 1
        break
print(i , j)