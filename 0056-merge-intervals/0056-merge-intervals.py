class Solution(object): 

    def merge(self, intervals):
        intervals.sort() 

        if len(intervals) == 1 : 
            return intervals 

        ans = [intervals[0]]
        for i in range (1, len(intervals)): 
            if intervals[i][0] > ans[-1][1]: 
                ans.append(intervals[i])

            else: 
                new = [min(intervals [i][0], ans[-1][0]), max(intervals[i][1], ans[-1][1])]
                ans.pop()
                ans.append(new)

        return ans