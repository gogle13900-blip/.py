n = int(input())

fib = [1, 2]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])

if fib[-1] > n:
    fib.pop()

r = []
rm = n
i = len(fib) - 1

while rm > 0 and i >= 0:
    if fib[i] <= rm:
        r.append(fib[i])
        rm -= fib[i]
        i -= 2
    else:
        i -= 1

with open("output3.txt", "w") as f:
    f.write(' '.join(map(str, r)))