num = int(input())
a = []


for i in range(num):
    x, y = list(map(int, input().split(" ")))
    a.append([x, y])
 
b= sorted(a)

for i in b:
    print(i[0],i[1] )
