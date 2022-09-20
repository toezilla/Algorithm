if __name__ == "__main__":
    n = int(input())
    balls = input()

    count = []
    tmp = balls.rstrip('R')
    count.append(tmp.count('R'))

    tmp = balls.rstrip('B')
    count.append(tmp.count('B'))

    tmp = balls.lstrip('R')
    count.append(tmp.count('R'))

    tmp = balls.lstrip('B')
    count.append(tmp.count('B'))

    print(min(count))
    