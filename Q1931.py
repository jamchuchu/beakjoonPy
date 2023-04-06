
num = int(input())
a= []
end = []

for _ in range(num):
    a.append(list(map(int, input().split(" "))))

a.sort(key =lambda x: x[0])
print(a)
a.sort(key = lambda x: x[1])
print(a)

last = 0
count = 0

for i, j in a:
    if i >= last:
        count += 1 
        last = j

print(count)

#--------------------------------------------------------------

# for i in range(num):
#     end.append(a[i][1])

# mx = max(end)+1

# answer = []

# for k in range(num+1):
#     room = [0 for _ in range(mx)]
#     for j in range(k, num):
#         start = a[j][0]
#         fi = a[j][1]

#         if room[start+1:fi+1] == [0 for _ in range(fi-start)]:
#             room[start:fi+1] = [j+1 for _ in range(fi+1-start)]


#     for j in range(0, k):
#         start = a[j][0]
#         fi = a[j][1]

#         if room[start:fi+1] == [0 for _ in range(fi+1-start)]:
#             room[start:fi+1] = [j+1 for _ in range(fi+1-start)]

#     print(k, room)
#     temp = []
#     for i in range(mx):
#         if room[i] != 0 and room[i] not in temp:
#             temp.append(room[i])
            


#     answer.append(len(temp))
    

# print(max(answer))
    

