class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        val=0

        for i in range(len(s)):
            val=val+dict1[s[i]]
            if i!=0:
                if dict1[s[i]]>dict1[s[i-1]]:
                    val=val-2*(dict1[s[i-1]])
        return val 