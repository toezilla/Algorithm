class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10

        start_number = 10 ** (length-1)
        quotient, remainder = divmod(n, length)

        if remainder == 0:
            return int(str(start_number + quotient-1)[-1])
        else:
            return int(str(start_number + quotient)[remainder-1])