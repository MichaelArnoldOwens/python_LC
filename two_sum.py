class Solution:
    def twoSum(self, nums, target: int):
        dictionary = dict()
        for i in range(len(nums)):
            curr = nums[i]
            print(curr)
            comp = target - curr
            print(comp)
            if dictionary.get(curr) != None:
                return [dictionary.get(curr), i]
            else:
                dictionary[comp] = i
        return None


solve = Solution()
print(solve.twoSum([2,7,11,15], 17))
