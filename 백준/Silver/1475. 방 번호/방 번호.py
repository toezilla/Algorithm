if __name__ == "__main__":
    numbers = input()
    
    arr = [0] * 10
    
    for number in numbers:
        if number == '9':
            arr[6] += 1
        else:
            arr[int(number)] += 1
    
    if arr[6]%2 == 0:
        arr[6] = arr[6]//2
    else:
        arr[6] = arr[6]//2+1
    
    print(max(arr))
        