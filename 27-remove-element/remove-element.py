class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        lastLegitimateIndex = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                lastLegitimateIndex += 1
                nums[lastLegitimateIndex] = nums[i]

        return len(nums) - count
