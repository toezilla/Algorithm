def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(n, r):
    return factorial(n)//(factorial(n-r) * factorial(r))

if __name__ == "__main__":
    n, r = map(int, input().split())
    print(combination(n, r))
    