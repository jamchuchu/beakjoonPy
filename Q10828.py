num= int(input())

a = []
st= ""
for _ in range(num):
    q = input().split(" ")
    if q[0] == "push":
        a.append(int(q[1]))
    elif q[0] == "pop":
        if len(a) == 0:
            st += str(-1)+ "\n"
        else:
            b = a.pop(-1)
            st += str(b)+ "\n"
            
    elif q[0] == "size":
        st += str(len(a))+ "\n"

    elif q[0] == "empty":
        if len(a) == 0:
            st += str(1) + "\n"

        else:
            st += str(0)+ "\n"
    elif q[0] == "top":
        if len(a) != 0:
            st += str(a[-1])+ "\n"
        else:
            st += str(-1)+ "\n"

print(st)