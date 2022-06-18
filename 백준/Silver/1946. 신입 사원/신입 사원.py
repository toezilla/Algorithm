import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = []
        for _ in range(n):
            paper, interview = map(int, input().split())
            array.append((paper, interview))
        array.sort(key = lambda x: x[0])
        
        # 이중 for 문 완전탐색 > O(n^2) -> 시간초과
        # minumum 변수 도입 > O(n)
        answer = 1
        minimum = array[0][1]
        for i in range(1, n):
            if (now:=array[i][1]) < minimum:
                answer +=1
                minimum = now
        
        print(answer)
        