N = int(input())
arr = []

for i in range(N):
    w, h = map(int, input().split())
    arr.append([w, h])

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt+1, end=" ")
