num =  int(input())

for _ in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))

    r = pow(x2-x1 , 2) + pow(y2-y1 , 2)
    r3 = pow(r, 0.5)

    maxN = max(r1, r2)
    minN = min(r1, r2)
    sumN  = r1 + r2
    subN = maxN -minN

    answer = 99

    if r3 > sumN:
        answer = 0
    elif maxN - minN < r3 < sumN:
        answer = 2
    elif 0 < r3 < maxN or (r3 == 0 and r1 != r2):
        answer = 0
    elif r3 == sumN or r3 == maxN - minN:
        answer= 1
    elif r3 == 0 and r1 == r2:
        answer = -1


    if r3 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r3 == sumN or r3 == subN:
            print(1)
        elif r3 < sumN and r3 > subN:
            print(2)
        else:
            print(0)

