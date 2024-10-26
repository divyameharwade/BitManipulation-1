# Time complexity - O(logn)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ldividend = abs(dividend)
        ldivisor = abs(divisor)
        res = 0
        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        while ldividend >= ldivisor:
            shifts = 1
            while (ldividend >= (ldivisor << shifts)):
                shifts += 1
            shifts -= 1
            res += 1 << shifts
            ldividend = ldividend - (ldivisor << shifts)
        if (dividend < 0) and (divisor > 0): return -res
        if (dividend > 0) and (divisor < 0): return -res
        return res
