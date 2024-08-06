class Solution(object):
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder( zip(*matrix)[::-1])

    def turnRight(self, vector): 
        return (vector[1], -1 * vector[0])