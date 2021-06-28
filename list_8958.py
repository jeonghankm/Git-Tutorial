tc = int(input())
for i in range(tc) :
    cnt = 0
    result = 0
    q = list(input())
    for j in range(len(q)) :
        if(q.pop() == "O") :
            cnt += 1
        else :
            cnt = 0
        result += cnt
    print(result)