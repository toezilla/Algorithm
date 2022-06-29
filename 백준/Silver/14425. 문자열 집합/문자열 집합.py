import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    answer = 0
    s_dict = {}
    
    for _ in range(n):
        word = input()
        if (first:=word[0]) in s_dict:
            s_dict[first].append(word)
        else:
            s_dict[first] = [word]
    
    for _ in range(m):
        compare = input()
        if (pre:=compare[0]) in s_dict:
            if compare in s_dict[pre]:
                answer+=1
    
    print(answer)
