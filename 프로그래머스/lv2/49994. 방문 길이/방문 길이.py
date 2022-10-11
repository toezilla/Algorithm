from typing import Tuple

def direction(x: str) -> Tuple:
    if x == 'U':
        return ((0, 1))
    if x == 'D':
        return ((0, -1))
    if x == 'R':
        return ((1, 0))
    if x == 'L':
        return ((-1, 0))

def solution(dirs: str) -> int:
    answer = 0
    visited = set()
    cur_x, cur_y = 5, 5
    
    for dir in dirs:
        opr = direction(dir)
        next_x = cur_x + opr[0]
        next_y = cur_y + opr[1]

        if 0<=next_x<11 and 0<=next_y<11:
            if ((cur_x, cur_y), (next_x, next_y)) not in visited:
                answer += 1
                visited.add(((cur_x, cur_y), (next_x, next_y)))
                visited.add(((next_x, next_y), (cur_x, cur_y)))
            cur_x, cur_y = next_x, next_y
            
    return answer