from typing import List

def find_dwarf(array: List) -> List:
    for i in range(9):
        for j in range(i + 1, 9):
                answer = []
                total = 0
                for n in range(9):
                    if n == i or n == j:
                        pass
                    else:
                        total += array[n]
                        if total > 100:
                            break
                        answer.append(array[n])
                if total == 100:
                    answer.sort()
                    return answer


if __name__ == "__main__":
    array = []
    for _ in range(9):
        array.append(int(input()))

    array.sort(reverse=True)
    print(*find_dwarf(array))

