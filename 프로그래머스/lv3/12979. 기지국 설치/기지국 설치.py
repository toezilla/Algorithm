def solution(n, stations, w):
    answer = 0
    available = []
    blank = []
    
    for station in stations:
        available.append((station-w, station+w))
    
    if available[0][0] > 0:
        blank.append(available[0][0]-1)
    
    for i in range(len(stations) - 1):
        if available[i+1][0] > available[i][1]:
            blank.append(available[i+1][0] - available[i][1]-1)
    
    if available[-1][-1] < n:
        blank.append(n - available[-1][-1])
    
    for x in blank:
        if x % (tmp:=2*w+1) == 0:
            answer += x//tmp
        else:
            answer += x//tmp + 1

    return answer