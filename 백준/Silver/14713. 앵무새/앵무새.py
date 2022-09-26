from collections import deque


if __name__ == "__main__":
    n = int(input())
    sentences = []
    for _ in range(n):
        sentences.append(deque(input().split()))
    messages = input().split()

    removed = []
    for message in messages:
        for sentence in sentences:
            if sentence and message == sentence[0]:
                sentence.popleft()
                removed.append(message)
                break

    for i in range(n):
        if sentences[i]:
            print('Impossible')
            exit()
    if messages != removed:
        print('Impossible')
        exit()

    print('Possible')