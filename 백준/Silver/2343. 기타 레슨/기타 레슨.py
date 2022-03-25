def Count(value):
    cnt = 1
    Sum = 0
    for x in arr:
        if Sum+x > value:
            cnt+=1
            Sum=x
        else:
            Sum+=x
    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    maxx = max(arr)
    lt = 1
    rt = sum(arr)
    res = 0
    
    while lt <= rt:
        key = (lt+rt)//2
        if key>=maxx and Count(key)<=m:
            res = key
            rt = key-1
        else:
            lt = key+1
    
    print(res)