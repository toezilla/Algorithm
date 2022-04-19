from collections import deque
n = int(input())
arr = list(map(int, input().split()))
stack = []
res = [-1]*n
stack.append(0)

for i in range(1, n):
    while stack and arr[i] > arr[stack[-1]]:
        res[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

for i in range(n):
    print(res[i])