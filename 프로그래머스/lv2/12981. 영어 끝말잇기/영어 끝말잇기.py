def solution(n, words):
    answer = []
    word_set = set()
    count = 0
    last_word = words[0][0]
    for word in words:
        if word in word_set or word[0] != last_word:
            return [count%n+1, count//n+1]
        
        count+=1
        word_set.add(word)
        last_word = word[-1]
    
    return [0, 0]
    