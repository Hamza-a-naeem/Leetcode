class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCased = s.lower()
        print(lowerCased)
        cleansedText = []
        for i in lowerCased:
            if i.isalnum():
                cleansedText.append(i)

        s = "".join(cleansedText)
        print(s)
        reversedText = s[::-1]

        if s == reversedText:
            return True
        return False

        