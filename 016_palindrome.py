class Solution:
    def isPalindrome(self, s: str) -> bool:
        lead_index = 0
        trailing_index = len(s) - 1
        while lead_index < trailing_index:
            if not s[lead_index].isalnum():
                lead_index += 1
                continue
            if not s[trailing_index].isalnum():
                trailing_index -= 1
                continue
            if s[lead_index].lower() != s[trailing_index].lower():
                return False
            else:
                lead_index += 1
                trailing_index -= 1
        return True
