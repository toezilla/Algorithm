if __name__ == "__main__":
    IPv6 = input().split(':')
    if '' in IPv6:
        if IPv6.index('')!=0 and IPv6[-1]=='':
            IPv6.remove('')
        idx = IPv6.index('')
        part1 = IPv6[:idx]
        part2 = IPv6[idx+1:]
        size = len(part1)+len(part2)
        for _ in range(8-size):
            part1.append('0000')
        IPv6 = part1+part2
    for i in range(8):
        if len(IPv6[i])<4:
            IPv6[i] = '0'*(4-len(IPv6[i]))+IPv6[i]

    for i in range(8):
        if i == 7:
            print(IPv6[i])
        else:
            print(IPv6[i], end=':')