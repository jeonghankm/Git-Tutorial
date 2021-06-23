n = int(input())
arr = list(map(int,input().split()))
arr.sort()

print(str(arr[0]) + " " + str(arr[int(n)-1]))