a = list(map(int, input().split()))
m = sum(a) / len(a)
r = []

for i, x in enumerate(a, 1):
    if x > m:
        d = x - m
    else:
        d = m - x
    if m != 0 and d / m > 1:
        r.append(i)

with open("output.txt", "w") as f:
    if r:
        f.write(' '.join(map(str, r)))
    else:
        f.write("NORMAL")