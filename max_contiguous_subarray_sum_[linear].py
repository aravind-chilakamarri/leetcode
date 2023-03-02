class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        max_so_far = nums[0]
        max_endings_here = nums[0]
        for i in range(1, len(nums)):
            max_endings_here = max(max_endings_here + nums[i], nums[i])
            max_so_far = max(max_so_far,max_endings_here)
        return max_so_far
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))