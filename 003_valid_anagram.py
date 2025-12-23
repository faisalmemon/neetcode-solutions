class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = [letter for letter in s]
        second = [letter for letter in t]
        first.sort()
        second.sort()

        if len(first) != len(second):
            return False
        
        for (index, char) in enumerate(first):
            if first[index] != second[index]:
                return False
        
        return True
