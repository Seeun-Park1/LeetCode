class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum(root, currSum):
            if not root: 
                return 0
            currSum = currSum * 10 + root.val
            if not root.left and not root.right: 
                return currSum
            return sum(root.left, currSum) + sum(root.right, currSum)
        return sum(root, 0)