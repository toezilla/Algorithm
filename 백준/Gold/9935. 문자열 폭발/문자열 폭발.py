if __name__ == "__main__":
    str = input()
    bomb = input()
    check = bomb[::-1]

    stack = []
    for x in range(len(str)):
        if len(stack) >= len(check)-1:
            if str[x] == check[0]:
                cnt = 1
                for i in range(1, len(check)):
                    if stack[-i] == check[i]:
                        cnt += 1
                if cnt == len(check):
                    for i in range(len(check)-1):
                        stack.pop()
                    continue

        stack.append(str[x])

    answer = ''
    if stack:
        for x in stack:
            answer = answer + x
        print(answer)
    else:
        print('FRULA')
