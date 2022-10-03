n = int(input())
arr_w = []
arr_h = []
res = [0]*n

for _ in range(n):
    w, h = map(int, input().split())
    arr_w.append(w)
    arr_h.append(h)

max_h = max(arr_h)
max_w = max(arr_w)


for i in range(n):
    cnt = 1
    wt = arr_w[i]
    ht = arr_h[i]
    
    for j in range(n):
        if arr_w[j]>wt and arr_h[j]>ht:
            cnt += 1

    res[i] = cnt

for i in res:
    print(i, end = ' ')