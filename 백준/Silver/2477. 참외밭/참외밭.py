melon = int(input())
values = [input().split() for _ in range(6)]
directions = [int(v[0]) for v in values]
lengths = [int(v[1]) for v in values]
max_lengths, box_lengths = [], []

for i in range(1, 5):
    if directions.count(i) == 1:
        max_lengths.append(lengths[directions.index(i)])
        temp = directions.index(i) + 3
        if temp >= 6:
            temp -= 6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)