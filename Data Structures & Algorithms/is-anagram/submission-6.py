class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = dict(Counter(s))
        for ch in t:
            if ch in char_dict:
                char_dict[ch]-=1
            else: 
                return False
        if any(char_dict.values()):
            return False
        return True