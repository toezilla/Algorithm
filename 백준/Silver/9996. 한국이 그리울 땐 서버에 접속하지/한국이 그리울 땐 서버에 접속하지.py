import re

if __name__ == "__main__":
    n = int(input())
    left, right = input().rstrip().split("*")
    pattern = re.compile(left+".*"+right+"+")

    for _ in range(n):
        name = input().rstrip()
        res = pattern.search(name)
        
        if res and res.group() == name:
            print('DA')
            
        else:
            print('NE')