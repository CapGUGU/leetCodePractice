class Solution(object):
    def arraySign(self, nums):
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                sign = sign * -1
        return sign