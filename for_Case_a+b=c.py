t = int(input())
#Case #1: 1 + 1 = 2
for i in range(1, t+1):
    a , b= map(int, input().split())
    print("Case #%d: " %i + str(a) + " + " + str(b) + " = " + str(a+b) )
