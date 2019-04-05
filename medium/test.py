def getbits(s, e):
    r = 0
    for i in range(s, e+1):
        r += pow(2, i)
    return r


a = getbits(0, 30)
b = getbits(5, 10)
c = getbits(15, 20)
d = b | c
e = getbits(16, 18)
print(a)
print("b", b)
print(c)
print(~a & b)
print(~b & c)
print("b", b)
print(d)
print(e)
print(~d & e)
