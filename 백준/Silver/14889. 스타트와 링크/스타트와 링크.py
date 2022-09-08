import sys
from itertools import combinations

def score(team):
    result = 0
    team = set(team)
    for player in team:
        for i in range(n):
            if i in team:
                result += table[player][i]
    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    
    n = int(input())
    table = []
    players = []
    for i in range(n):
        table.append(list(map(int, input().split())))
        players.append(i)

    comb_list = list(combinations(players, n // 2))
    answer = 2147000000

    for item in comb_list:
        team_a = list(item)
        team_b = list(set(players) - set(team_a))
        if (tmp := abs(score(team_a) - score(team_b))) < answer:
            answer = tmp

    print(answer)
