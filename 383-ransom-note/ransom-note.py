class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mega_hash ={}

        for c in magazine: 
            mega_hash[c] = 1 + mega_hash.get(c, 0)

        for c in ransomNote: 
            if c not in mega_hash or mega_hash[c] <= 0: 
                return False 

            mega_hash[c] -= 1 

        return True