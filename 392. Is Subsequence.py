str1 = "acb"
str2 = "ahbgdc"
str3 = ""
for s in str1:
    if s in str2:
        str3 += s
if str1 == str3:
    print("true") 
else:
    print("false")