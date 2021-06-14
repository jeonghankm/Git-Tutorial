t = int(input())
# Case #1: 2
# Case #2: 3
for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #%d:" %i + " "+str(a +b))
