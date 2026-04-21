class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST={} 
        mapTS={}
        for char_s,char_t in zip(s,t):
            if char_s in mapST and mapST[char_s]!=char_t:
                return False
            if char_t in mapTS and mapTS[char_t]!=char_s:
                return False
            mapST[char_s]=char_t
            mapTS[char_t]=char_s
        return True 

print(Solution().isIsomorphic("egg","add"))
