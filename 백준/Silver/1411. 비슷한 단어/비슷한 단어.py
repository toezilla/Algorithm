import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    array = []
    
    for _ in range(n):
        array.append(input())

    cnt = 0
    length = len(array[0])
    for i in range(n-1):
        main = array[i]
        
        for j in range(i+1, n):
            string = array[j]
            dict = {}
            
            for k in range(length):
                s, m = string[k], main[k]
                
                if s in dict.keys():
                    if dict[s] == m:
                        continue
                    else:
                        break
                else:
                    if m not in dict.values():
                        dict[s] = m
                    else:
                        break
            else:
                cnt+=1
    print(cnt)
