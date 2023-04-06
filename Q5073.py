while True:
    x,y,z = input().split(" ")
    a = [x,y,z]
    a = list(map(int, a))

    # if x==y==z==0:
    #     break
    # if x==y==z:
    #     print("Equilateral")
    # elif x==y or x==z or y==z:
    #     print("Isosceles")
    # elif x != y != z:
    #     b = max(a)
    #     a.remove(b)
    #     if a[0]+a[1] > b:
    #         print("Scalene")
    #     else:
    #         print("Invalid")

    
    # 입력
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    # 삼각형 판별
    if a == b == c:
        print("Equilateral")
    elif 2 * max(a, b, c) >= a + b + c:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")


