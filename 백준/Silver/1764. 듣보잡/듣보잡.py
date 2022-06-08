if __name__ == "__main__":
    n, m = map(int, input().split())
    seen = {}
    answer = []
    
    for _ in range(n):
        seen[input()] = 1
    for _ in range(m):
        name = input()
        if name in seen:
            answer.append(name)
    answer.sort()
    print(len(answer))
    for x in answer: print(x)
