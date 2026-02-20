
x1, y1, x2, y2, x3, y3 = map(float, input().split())

d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
d2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

def f(n):
    if n.is_integer():
        return str(int(n))
    return str(n).rstrip('0').rstrip('.')

with open("output2.txt", "w") as out:
    if d1 < d2:
        out.write(f"{f(x2)}{f(y2)}")
    elif d2 < d1:
        out.write(f"{f(x3)}{f(y3)}")
    else:
        out.write(f"{f(x2)}{f(y2)}{f(x3)}{f(y3)}")