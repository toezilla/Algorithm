if __name__ == "__main__":
    n, l = map(int, input().split())
    pond = [list(map(int, input().split())) for _ in range(n)]
    pond.sort(key=lambda x: x[0])
    wood = pond[0][0]
    tot_cnt = 0
    
    for start, end in pond:
        if wood > end:
            continue
        elif wood < start:
            wood = start
        dist = end - wood
        flag = 1
        if dist%l == 0:
            flag = 0
        cnt = dist//l + flag
        wood+=cnt * l
        tot_cnt += cnt

    print(tot_cnt)
    