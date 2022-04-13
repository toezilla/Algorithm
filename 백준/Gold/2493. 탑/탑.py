n = int(input())
a = list(map(int, input().split()))

stack = []
res = [0]*n

for i in enumerate(a):
    idx = i[0]
    while stack:
        if i[1] >= stack[-1][1]:
            stack.pop()
        else:
            res[idx] = stack[-1][0]+1
            break
    stack.append(i)
print(*res)