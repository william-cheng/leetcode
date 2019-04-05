

def typein(s):
    r = []
    for c in s:
        if c == "#":
            r = r[:-1]
        else:
            r.append(c)
    return "".join(r)

print(typein("ab#c") == typein("ad#c"))
print(typein("") == typein("#"))
print(typein("a##c") == typein("#a#c"))
