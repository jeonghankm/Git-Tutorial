n = int(input())

if 1 <= n <= 100:
    for i in range(1, n + 1):
       print('*' * i)
else:
    print('1~100만 입력 ')
