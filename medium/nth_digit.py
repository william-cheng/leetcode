

def nth_digits(n):
    if n < 9:
        return n
    i = 0
    count = 0
    while count < n:
        count += 9 * pow(10, i) * (i + 1)
        i += 1
    i -= 1
    count = count - 9 * pow(10, i) * (i + 1)
    #i -= 1
    num = pow(10, i) - 1
    num += (n - count) / (i + 1)
    remain = (n - count) % (i + 1)
    print("n={}, num={}, count={}, i={}, remain={}".format(n, num, count, i, remain))
    if remain == 0:
        return num % 10
    else:
        return int(str(num + 1)[remain-1])

print(nth_digits(1000) == 3)
print(nth_digits(3) == 3)
print(nth_digits(11) == 0)
print(nth_digits(12) == 1)
print(nth_digits(100000000) == 8)
