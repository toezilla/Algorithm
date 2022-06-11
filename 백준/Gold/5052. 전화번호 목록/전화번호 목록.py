import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = [input().rstrip() for _ in range(n)]
        nums.sort()
        
        flag = True
        for i in range(n-1):
            length = len(nums[i])
            if nums[i] == nums[i+1][:length]:
                flag = False
                break
        if flag:
            print('YES')
        else:
            print('NO')