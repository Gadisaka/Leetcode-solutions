s = "abc"
t = "anboc"

def func(s,t):
    s_pointer = 0
    t_pointer = 0

    if len(s) == 0:
        return True
    while t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
            t_pointer += 1
        else:
            t_pointer += 1
        if s_pointer == len(s):
            return True
    return False

print(func(s,t))