

height = [8,7,2,1]

def func(height):

    l = 0
    r = len(height) - 1
    max_area = 0

    while l < r:
        area = (r - l) * min(height[l] , height[r])
        max_area = max(max_area , area)    

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area

print(func(height))