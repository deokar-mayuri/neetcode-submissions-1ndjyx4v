class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ""
        for char in s:
            if char.isalnum():
                alphanum += char.lower()
        
        return alphanum == alphanum[::-1]