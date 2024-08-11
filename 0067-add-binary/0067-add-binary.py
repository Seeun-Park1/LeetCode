class Solution(object):
    def addBinary(self, a, b):
        sum_binary = int(a, 2) + int(b, 2)
        return format(sum_binary, "b")
