num = []
numset = set(num)
longest = 0
for n in num:
    if (n - 1)not in numset:
        length = 0
        while (n + length) in numset:
            length += 1
        longest = max(longest , length)
print(longest)

