if __name__ == "__main__":
    notes = list(map(int, input().split()))
    status = -1
    for i in range(1, 8):
        if notes[i] > notes[i-1]:
            if status == 0:
                print("mixed")
                break
            else:
                status = 1
        else:
            if status == 1:
                print("mixed")
                break
            else:
                status = 0
    else:
        if status: print("ascending")
        else: print("descending")
            