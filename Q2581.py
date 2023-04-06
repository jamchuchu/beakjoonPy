x = int(input())
y = int(input())

num = x
z = 2
so = []

while x <= y:
    if z == x :
        so.append(x)
        x += 1
        z = 2
        continue

    if x==1 or x % z == 0:
        x += 1
        z = 2
        continue
    else:
        z += 1

if sum(so) == 0:
    print(-1)
else:
    print(sum(so))
    print(min(so))