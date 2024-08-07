class Solution(object):
    def combinationSum(self, candidates, target): 
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack): 
            if remain == 0: 
                result.append(stack)
                return 


            for item in candidates: 
                if item > remain: break 
                if stack and item < stack [-1]: continue
                else: 
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result