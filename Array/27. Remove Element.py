class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k


if __name__ =="__main__":
    
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 2))