def Fibonacci(x):
    arr = []
    for i in range(x+1):
        arr.append(i)
    arr[0] = 0
    arr[1] = 1
    for j in range(2, x+1):
        arr[j] = arr[j-1]+arr[j-2]
    return arr[x]

if __name__ == "__main__":
    print(Fibonacci(int(input())))