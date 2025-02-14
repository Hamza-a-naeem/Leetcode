class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        strVal = str(x)
        strList = list(strVal)

        l = 0
        r = len(strList) - 1

        for i in range(len(strList)/2):
            if strList[l] != strList[r]:
                return False      
            l += 1
            r -= 1  
        return True