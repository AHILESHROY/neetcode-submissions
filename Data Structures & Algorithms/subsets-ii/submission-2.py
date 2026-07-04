class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        curr = []

        def backtrack(index_nums):
                
                res.append(curr[:])
                

                for i in range(index_nums, len(nums)):
                    if i> index_nums and nums[i] == nums[i-1]:
                        continue
                    curr.append(nums[i])
                    backtrack(i+1)

                    curr.pop()

        backtrack(0)

        return res
