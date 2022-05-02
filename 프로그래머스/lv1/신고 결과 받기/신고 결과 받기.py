def solution(id_list, report, k):
    answer = []
    dict = {}
    check = {}
    for id in id_list:
        dict[id] = []
        check[id] = 0
    for string in report:
        From, To = map(str, string.split())
        if To in dict[From]:
            pass
        else:
            dict[From].append(To)
            check[To]+=1
        
    for id in id_list:
        tmp = 0
        for s in dict[id]:
            if check[s] >= k:
                tmp+=1
        answer.append(tmp)

    return answer
