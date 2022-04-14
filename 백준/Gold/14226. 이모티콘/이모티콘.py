from collections import deque

if __name__ == "__main__":
    s = int(input())
    duration = [[-1]*(s+1) for _ in range(s+1)]

    Queue = deque()
    Queue.append((1, 0))
    duration[1][0] = 0

    while Queue:
        current = Queue.popleft()
        screen = current[0]
        clipboard =  current[1]
        if duration[screen][screen] == -1:
            duration[screen][screen] = duration[screen][clipboard]+1
            Queue.append((screen, screen))
        if screen+clipboard <= s and duration[screen+clipboard][clipboard] == -1:
            duration[screen+clipboard][clipboard] = duration[screen][clipboard]+1
            Queue.append((screen+clipboard, clipboard))
        if screen-1>=0 and duration[screen-1][clipboard] == -1:
            duration[screen-1][clipboard] = duration[screen][clipboard]+1
            Queue.append((screen-1, clipboard))
    answer = -1
    for i in range(s + 1):
        if duration[s][i] != -1:
            if answer == -1 or answer > duration[s][i]:
                answer = duration[s][i]
    print(answer)