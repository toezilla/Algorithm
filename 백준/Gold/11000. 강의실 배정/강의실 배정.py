import heapq
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n = int(input())
    schedule = []
    classrooms = []
    
    for _ in range(n):
        start, end = map(int, input().split())
        schedule.append((start, end))
    
    schedule.sort(key= lambda x: x[0])
    
    for x in schedule:
        if classrooms and classrooms[0]<=x[0]:
            heapq.heappop(classrooms)
        heapq.heappush(classrooms, x[1])
        
    print(len(classrooms))
    