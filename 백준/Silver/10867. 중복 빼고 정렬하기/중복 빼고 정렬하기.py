if __name__ == "__main__":
    n = int(input())
    answer = set(map(int, input().split()))
    answer = list(answer)
    answer.sort()
    print(*answer)
    