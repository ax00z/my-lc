class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (len (nums) or target) == 0:
            return 0

        if target in nums:
            return nums.index(target)

        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
