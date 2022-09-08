def is_prime(number):
    for div in range(2, int(number**0.5)+1):
        if int(number) % div == 0:
            return False
    return True


def dfs(number):
    if len(str(number)) == n:
        print(number)
        return
    for i in range(10):
        if is_prime((tmp := number*10+i)):
            dfs(tmp)


if __name__ == "__main__":
    n = int(input())
    dfs(2)
    dfs(3)
    dfs(5)
    dfs(7)
