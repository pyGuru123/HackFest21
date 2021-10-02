"""
https://leetcode.com/problems/rotate-array/
"""


class Solution:
    @staticmethod
    def rotate(nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_nums = len(nums)
        k = k % total_nums
        # print(k)
        rotated = nums[total_nums - k:] + nums[:total_nums - k + 1]
        # print(rotated)
        for i in range(total_nums):
            nums[i] = rotated[i]


numbers = [1, 2, 3, 4, 5, 6, 7]

Solution.rotate(nums=numbers, k=3)
assert numbers == [5, 6, 7, 1, 2, 3, 4]
"""
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

numbers = [-1, -100, 3, 99]
Solution.rotate(nums=numbers, k=2)
assert numbers == [3, 99, -1, -100]
"""
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

"""
Follow up:

Try to come up with as many solutions as you can. 
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
