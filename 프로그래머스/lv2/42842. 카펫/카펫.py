def solution(brown, yellow):
    _sum = (brown + 4)//2
    _times = brown + yellow
    for i in range(1, _sum):
        if i * (_sum - i) == _times:
            return [max(i, _sum-i), min(i, _sum-i)]
    
