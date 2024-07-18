word1= 'abc'
word2= 'pq'

n1 = len(word1)
n2 = len(word2)
m = min(n1 , n2)
merged = ''
for i in range(m):
    merged += word1[i] + word2[i]
if n1 == n2:
    print (merged)
elif n1 > n2:
    print (merged + word1[m:])
else:
    print( merged + word2[m:])