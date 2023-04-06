a= input().split(" ")

i = 0

while i < len(a):
    if a[i] == "":
        a.pop(i)
    else:
        i+= 1


print(len(a))
