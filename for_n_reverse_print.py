n = int(input())

if 0 < n <= 100000:
    for i in range(n, 0, -1): #역순
        n -= 1
        print(i)
        if i == 1:
            break
