# 1071. Greatest Common Divisor of Strings

str1 = "Leet"
str2 = "code"

n1 = len(str1)
n2 = len(str2)
m = min(n1 , n2)

strSet = []

for i in range(m):
    if str1[i] == str2[i] and str1[i] not in strSet:
        strSet.append(str1[i])
print("".join(strSet))