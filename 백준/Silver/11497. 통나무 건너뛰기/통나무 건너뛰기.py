if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        trees = list(map(int, input().split()))
        trees.sort()
        answer = 0
        
        for i in range(2, n):
            answer = max(answer, abs(trees[i]-trees[i-2]))
        
        print(answer)
        