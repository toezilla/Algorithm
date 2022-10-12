def solution(A, B):
    A.sort()
    B.sort()
    
    answer = 0
    
    idx_B = 0
    for idx_A in range(len(A)):
        if idx_B == len(B):
            break
        
        while True:
            if idx_B == len(B):
                break
                
            if B[idx_B] > A[idx_A]:
                answer += 1
                idx_B += 1
                break
                
            idx_B += 1
        
    
    return answer