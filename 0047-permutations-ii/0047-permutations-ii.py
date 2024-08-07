class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res 

    def dfs(self, nums, path, res):
        if not nums: 
            res.append(path)
        for i in xrange(len(nums)): 
            if i > 0 and nums[i] == nums [i-1]:
                continue 
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res) 