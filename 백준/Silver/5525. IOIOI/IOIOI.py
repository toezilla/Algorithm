if __name__ == "__main__":
    n = int(input())
    m = int(input())
    s = input()

    idx = 0
    cnt = 0
    while idx < m-3:
        if s[idx:idx+3] == 'IOI':
            idx += 2
            o = 1
            while idx<m-2 and s[idx+1] == 'O' and s[idx+2] == 'I':
                idx+=2
                o+=1

            if o == n: cnt+=1
            elif o > n: cnt+=o-n+1
            idx+=1

        else:
            idx+=1

    print(cnt)