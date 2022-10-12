def dfs(numbers, target, depth, total):
    global count
    if depth == len(numbers):
        if total == target:
            count += 1
        return
    
    dfs(numbers, target, depth+1, total + numbers[depth])
    dfs(numbers, target, depth+1, total - numbers[depth])
    

def solution(numbers, target):
    global count
    
    count = 0
    dfs(numbers, target, 0, 0)
    
    return count