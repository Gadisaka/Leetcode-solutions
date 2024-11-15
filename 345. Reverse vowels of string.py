vowels = ['a' , 'A' , 'e' , 'E' , 'i' , 'I' , 'o' , 'O' , 'u' , 'U']
res = []
str1 = []

for ch in s:
    str1 += ch
    if ch in vowels:
        res.append(ch)

lenres = len(res) - 1

for i in range(len(s)):
    if str1[i] in vowels:
        str1[i] = res[lenres]
        lenres -= 1
        
return "".join(map(str,str1))