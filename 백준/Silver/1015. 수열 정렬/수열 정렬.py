if __name__ == "__main__":
    n = int(input())
    answer = []
    
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    
    for i in range(n):
        idx = sorted_a.index(a[i])
        answer.append(idx)
        sorted_a[idx] = -1
    print(*answer)

