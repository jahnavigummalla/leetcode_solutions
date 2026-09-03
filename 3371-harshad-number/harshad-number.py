class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        digit_sum = 0
        n = x
        while n > 0:
            digit_sum += n % 10
            n //= 10
        if x % digit_sum == 0:
            return digit_sum
        return -1 