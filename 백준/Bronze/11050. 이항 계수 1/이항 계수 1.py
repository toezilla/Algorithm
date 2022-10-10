def power(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

if __name__ == "__main__":
    n, k =map(int, input().split())
    res = power(n)//power(k)//power(n-k)
    print(res)