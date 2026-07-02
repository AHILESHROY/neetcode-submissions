class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def backtrack(index, curr_xor):
            nonlocal ans

            if index == len(nums):
                ans+=curr_xor
                return

            # Include nums[index]
            backtrack(index+1,curr_xor)

            # Exclude nums[index]
            backtrack(index+1,curr_xor^nums[index])
        backtrack(0, 0)
        return ans
