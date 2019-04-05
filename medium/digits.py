
def digits(i):
    d = [i % 10]
    r = i / 10
    while r:
        d.insert(0, r % 10)
        r = r / 10
    return d

print(digits(8))
print(digits(18))
print(digits(188))
