if __name__ == "__main__":
    n = int(input())
    array = []
    for i in range(n):
        x,y = map(int, input().split())
        array.append([x,y])
    
    array = sorted(array, key = lambda x : x[0])

    pop = 0
    for i in range(n):
        k = array[i][1]
        pop = pop + k

    mid = pop//2

    if (pop%2) != 0: 
        mid = mid + 1

    pop_count = 0
    for q,w in array:
        pop_count = pop_count + w
        if pop_count >= mid:
            res = q
            break
    print(res)