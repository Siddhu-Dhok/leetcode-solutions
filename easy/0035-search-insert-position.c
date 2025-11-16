# Problem: 35. Search Insert Position
# Difficulty: Easy
# URL: https://leetcode.com/problems/search-insert-position/

int searchInsert(int* nums, int numsSize, int target) {
    int i = 0;

    while (i < numsSize && nums[i] < target) {
        i++;
    }

    return i;
}
