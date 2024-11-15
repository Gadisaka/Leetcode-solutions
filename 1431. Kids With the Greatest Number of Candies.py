# 1431. Kids With the Greatest Number of Candies

candies = [2,3,5,1,3]
extraCandies = 3

max_candies = max(candies)

result = []
for i in candies:
    if i + extraCandies >= max_candies:
        result.append(True)
    else:
        result.append(False)

print(result)