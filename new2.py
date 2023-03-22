# class Q1:
#     n,m = map(int, input().split(' '))

#     bas = [i+1 for i in range(n)]

#     for i in range(m):
#         i, j = map(int, input().split(' '))
#         bas[i-1], bas[j-1] = bas[j-1], bas[i-1]

#     print(' '.join(map(str, bas)))

# class Q2562:
#     a = [int(input()) for i in range(9)]

#     print(max(a))
#     print(a.index(max(a))+1)


# class Q10811:
#     n,m  = map(int, input().split(" "))

#     a =  [i+1 for i in range(n)]

#     for i in range(m):
#         i, j  = map(int, input().split(' '))
#         for _ in range((j-i+1)//2):
#             a[i-1], a[j-1] = a[j-1], a[i-1]

#             i += 1
#             j -= 1

#     print(" ".join(map(str, a)))

# class Q10807:
#     num =  input()
#     a = list(map(int, input().split(" ")))

#     num2 = int(input())    

#     count = 0
#     for i in a:
#         if i == num2:
#             count += 1
#     print(count)

    # b = filter(lambda x:x==int(num2), a)
    # print(len(list(b)))

    # def ans(a, list):
    #     count = 0 
    #     for i in range(list):
    #         if i == a:
    #             count += 1
    #     return count

# class Q10871:
#     global y
#     x, y = map(int, input().split(" "))

#     a = list(map(int, input().split(' ')))
    
#     b = list(filter(lambda x : x < y, a))

#     for i in b:
#         print(i, end=" ")

class Q10810:
    x, y  = map(int, input().split(" "))
    
    a = [0 for _ in range(x)]

    for _ in range(y):
        b =list(map(int, input().split(" ")))
        for i in range(b[0]-1, b[1]):
            a[i] = b[2]

    for i in a:
        print(i, end=" ")