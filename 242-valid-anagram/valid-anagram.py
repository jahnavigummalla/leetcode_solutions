class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}
        f2={}
        for char in s:
            if char in f1:
                f1[char]+=1
            else:
                f1[char]=1
        for char in t:
            if char in f2:
                f2[char]+=1
            else:
                f2[char]=1 
        if f1==f2:
            return True
        else:
            return False