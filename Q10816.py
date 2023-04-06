input()
a =  list(map(int, input().split(" ")))
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

input()
answer =  list(map(int, input().split(" ")))

for i in answer:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")