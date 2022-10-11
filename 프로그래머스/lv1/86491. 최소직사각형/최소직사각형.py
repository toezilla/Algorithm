def solution(sizes):
    answer = 0
    # 1. sizes를 탐색하면서
    ## 1-1. 세로가 가로보다 길면 교체
    ## 1-2. 세로, 가로의 최댓값 최신화
    
    max_width = -1
    max_height = -1
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])

    # 2. 세로의 최댓값 X 가로의 최댓값
    answer = max_width * max_height
    return answer