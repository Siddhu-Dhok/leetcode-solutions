# Problem: 26. Remove Duplicates From Sorted Array
# Difficulty: Easy
# URL: https://leetcod.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0  # pointer for the place to insert the next unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # overwrite with the next unique value

        return i + 1  # length = index + 1


#need to work on the logic
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if (len(nums) == 1 or (len(nums) ==2 and nums[0] == nums[1])):
#             return 1
#         i = 0
#         j = 1
#         a = nums[0]
#         b = nums[1]
#         max = len(nums)
#         flag = 0
#         flag2 = 0

#         for k in range(max - 1):
#             if (nums[k] != nums[k + 1]):
#                 flag2 = 1
#                 break

#         if not flag2:
#             return 1

#         while (a <= b):
#             a = nums[i]
#             b = nums[j]
#             if (a == b):
#                 nums.remove(b)
#                 nums.append(b)
#                 flag = 1

#             if (a != b):
#                 i += 1
#                 j += 1
#             if j == max:
#                 if not flag:
#                     i += 1
#                 break

#         return i 
