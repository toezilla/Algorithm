if __name__ == "__main__":
    n = int(input())
    trees = list(map(int, input().split()))
    tree_sum = sum(trees)
    cnt = tree_sum // 3
    
    if tree_sum % 3 != 0:
        print('NO')

    else:
        for tree in trees:
            cnt -= tree//2
        if cnt>0:
            print('NO')
        else:
            print('YES')