class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort() 
        def dfs(target, path, nums, idx, res): 
            if target == 0: 
                res.append(path)
            if target <= 0: 
                return 
            for i in range(idx, len(nums)):
                if i>idx and nums[i] == nums[i-1]:
                    continue
                dfs(target-nums[i], path+[nums[i]], nums, i+1, res)
        
        res = []
        dfs(target, [], candidates, 0, res)
        return res
        