import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    word_count = {}
    answer = []
    for _ in range(n):
        word = input().rstrip()
        if (length := len(word)) >= m:
            if word in word_count:
                word_count[word] += 1
                continue
            word_count[word] = 1
            answer.append([word, length])

    for chunk in answer:
        if chunk[0] in word_count:
            chunk = chunk.append(word_count[chunk[0]])

    answer.sort(key = lambda x: (-x[2], -x[1], x[0]))

    for chunk in answer:
        print(chunk[0])
        