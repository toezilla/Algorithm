import sys
input = sys.stdin.readline

def Counter(x):
    cnt = 1
    start = Point[0]
    for i in range(1, n):
        if Point[i] - start >= x:
            cnt+=1
            start = Point[i]
    return cnt

n, c = map(int, input().split())
Point = []
for _ in range(n):
    Point.append(int(input()))

Point.sort()
lt = 1
rt = Point[-1]


while lt <= rt:
    key = (lt+rt)//2
    if Counter(key) >= c:
        res = key
        lt = key+1
    else:
        rt = key-1

print(res)