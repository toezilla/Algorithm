def hansoo(number: int):
    answer = 0
    number = str(number)
    # if number < 100
    if len(number) <= 2:
        answer = int(number)
        return answer

    # if number >= 100
    answer += 99
    for num in range(100, int(number)+1):
        num = str(num)
        diff = int(num[0]) - int(num[1])
        for i in range(1, len(num)-1):
            if int(num[i]) - int(num[i+1]) == diff:
                answer += 1
    return answer


if __name__ == "__main__":
    number = int(input())
    print(hansoo(number))