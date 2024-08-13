if len(s) == 0 :
    return True

t_pointer = 0
s_pointer = 0

while t_pointer < len(t):
    if t[t_pointer] == s[s_pointer] :
        s_pointer += 1

        if s_pointer == len(s):
            return True
    t_pointer += 1
return False