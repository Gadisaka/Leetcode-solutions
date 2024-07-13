num = [0,3,7,2,5,8,4,6,0,1]

unique = list(set(num))
s = sorted(unique)

print(unique)
print(s)

if not unique:
    res = 0
else:
    res = 1

for i in range(len(s) - 1):
    if s[i+1] - 1 == s[i] and s.index(s[i+1]) <= len(s) - 1:
        res+=1

print(res)
