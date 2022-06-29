def multiple(a, n):
    if n == 1:
        return a%c
    else:
        tmp = multiple(a, n//2)
        if n%2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(multiple(a, b))
    