s = input()
num_of_a = s.count('a')

res = len(s)
for i in range(num_of_a - 1, len(s)):
    res = min(res, s[i - num_of_a + 1:i + 1].count('b'))

for i in range(0, num_of_a - 1):
    res = min(res, (s[i - num_of_a + 1:] + s[:i + 1]).count('b'))

print(res)