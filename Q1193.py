# a= []

# mx = int(input())

# num = 1
# i = 1

# while num < mx:
#    a.append(num)
#    i += 1
#    num += i

# leng = len(a)+1
# answer = []

# if leng%2 == 1:
#    for j in range(leng):
#         answer.append(str(leng-j)+"/"+str(j+1))
# else:
#     for j in range(leng):
#         answer.append(str(j+1)+"/"+str(leng-j))



# if mx == 1:
#     idx = 0
# else:
#     idx = mx-a[-1]-1

# print(answer[idx])


X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')