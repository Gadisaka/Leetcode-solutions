prices = [2,4,1]

def fun():
    left = 0
    right = 1
    maxp = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxp = max(maxp , profit)
        else:
            left = right
        right += 1
    return maxp

result = fun()
print(result)