def hansoo(N):
    answer_list = []
    for i in range(1, N+1):
        number_list = list(map(int, str(i)))
        
        if 1 <= i < 10:
            answer_list.append(0)
        elif 10 <= i < 100:
            answer_list.append(1)
        elif 100 <= i < 1000:
            if number_list[1] - number_list[0] == number_list[2] - number_list[1]:
                answer_list.append(2)
            else:
                pass
        else:
            pass
    print(len(answer_list))
            
hansoo(int(input()))