#n, x = int(input())
#10, 5
n = input()
x = input()

n = n.split()
x = x.split()
for i in x:
    if int(i) < int(n[1]):
        print(i, end=" ")