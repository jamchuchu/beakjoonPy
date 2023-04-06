a = list(map(int, input()))

b = sorted(a)

for i in reversed(b):
    print(i, end="")