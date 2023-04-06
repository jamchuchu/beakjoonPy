x, y = map(int, input().split(" "))

if y> 44:
    y -= 45
else:
    y = y+60-45
    if x==0:
        x= 23
    else:
        x-= 1

print(x,y)

