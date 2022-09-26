if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    stack = []
    answer = [0] * n

    for i in enumerate(a):
        idx = i[0]
        while stack:
            if i[1] >= stack[-1][1]:
                stack.pop()
                continue
            answer[idx] = stack[-1][0]+1
            break
            
        stack.append(i)
        
    print(*answer)
    