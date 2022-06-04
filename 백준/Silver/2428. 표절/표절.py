if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    total_cnt = 0

    for i in range(n-1):
        start = i+1
        end = n-1
        cnt = -1
        while start <= end:
            key = (start+end)//2
            if numbers[i] >= numbers[key] * 0.9:
                cnt = key
                start = key+1
            else:
                end = key-1
        
        total_cnt += cnt-i if cnt > -1 else 0

    print(total_cnt)