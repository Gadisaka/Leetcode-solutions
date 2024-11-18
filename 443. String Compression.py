# 443. String Compression
chars= ["a","b","b","b","b","b","b","b","b","b"]


def func(chars):
    if len(chars) < 2:
        return len(chars)
    i = 1
    count = 1

    while i < len(chars):
        if chars[i] == chars[i - 1]:
            count += 1
            chars.pop(i)
        else:
            if count > 1:
                for j in str(count):
                    chars.insert(i , j)
                    i += 1
                count = 1
            i += 1
    
    if count > 1:
        for j in str(count):
                    chars.append(j)

    return len(chars) , chars
                

    



print(func(chars))
