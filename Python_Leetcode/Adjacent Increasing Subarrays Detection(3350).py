'''

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109


'''

class Solution:
 def maxIncreasingSubarrays(self, nums: List[int]) -> int:
    
    n = len(nums)
    inc = [1] * n

    # Step 1: Preprocess increasing lengths
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            inc[i] = inc[i + 1] + 1

    # Step 2: Binary search for max k
    def is_valid(k):
        for i in range(n - 2 * k + 1):
            if inc[i] >= k and inc[i + k] >= k:
                return True
        return False

    left, right = 1, n // 2
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res



'''

or 

'''


from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        pre = 0   # length of previous increasing segment
        cur = 0   # length of current increasing segment
        mx = 0    # max k found

        n = len(nums)
        for i in range(n):
            cur += 1
            # If end of array or next element breaks strictly increasing order
            if i == n - 1 or nums[i] >= nums[i + 1]:
                # Check possible maximum k from either splitting current segment or combining with previous segment
                mx = max(mx, cur // 2, min(pre, cur))
                pre = cur
                cur = 0

        return mx


