from itertools import permutations

def solution(k, dungeons):
    answer = -1
    trials = list(permutations(dungeons, len(dungeons)))
    
    max_count = 0
    for trial in trials:
        life = k
        count = 0
        for dungeon in trial:
            if life >= dungeon[0]:
                count += 1
                life -= dungeon[1]
        max_count = max(max_count, count)
    
    return max_count