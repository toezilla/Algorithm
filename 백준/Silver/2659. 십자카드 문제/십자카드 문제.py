def find_clocknum(number):
    answer = number
    tmp = number
    for _ in range(3):
        first = tmp // 1000
        tmp = (tmp - first * 1000) * 10 + first
        if tmp < answer:
            answer = tmp

    return answer

if __name__ == "__main__":
    clocknums = set()

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    number = i*1000 + j*100 + k*10 + l
                    clocknums.add(find_clocknum(number))
    clocknums = list(clocknums)
    clocknums.sort()

    array = list(map(int, input().split()))
    num = find_clocknum(array[0]*1000 + array[1]*100 + array[2]*10 + array[3])
    print(clocknums.index(num)+1)
    