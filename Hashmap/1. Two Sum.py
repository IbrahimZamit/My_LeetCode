# Problem_Description
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    # # Lets try the Brute_Force solution first / O(n*2)
    # def twoSum(self, nums, target):
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if target == nums[i] + nums[j]:
    #                 return [i, j] 
    #     return False

    # Now we try to improve the solution by using a hashmap / O(n)
    def twoSum(self, nums, target):
        temp_dict = {}

        for i, value in enumerate(nums):
            complement = target - value
            if complement in temp_dict:
                return [temp_dict[complement], i]
            temp_dict[value] = i
        return None

if __name__=="__main__":

    # Create an instance of the Solution class
    sol = Solution()

    # Call the twoSum function and print the result
    print(sol.twoSum([2,7,11,15], 9))  # Output: [0, 1]