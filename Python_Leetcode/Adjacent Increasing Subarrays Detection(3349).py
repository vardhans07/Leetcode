'''
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

 

Constraints:

2 <= nums.length <= 100
1 < 2 * k <= nums.length
-1000 <= nums[i] <= 1000

'''

class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        pre = 0               #pre: stores length of previous increasing sequence
        cur = 1                #cur: starts at 1 because we begin with one element
        max_valid = 0         #max_valid: tracks the best possible length that could represent two adjacent increasing subarrays

        for i in range(1, len(nums)):    #We loop from index 1 to end of array.
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                max_valid = max(max_valid, cur // 2, min(pre, cur))
                pre = cur
                cur = 1

        max_valid = max(max_valid, cur // 2, min(pre, cur))
        return max_valid >= k
'''
Explanation  ----->>
i = 1 → nums[1] = 5 > nums[0] = 2
cur += 1 → cur = 2
i = 2 → nums[2] = 7 > nums[1] = 5
cur += 1 → cur = 3
i = 3 → nums[3] = 8 > nums[2] = 7
cur += 1 → cur = 4
i = 4 → nums[4] = 9 > nums[3] = 8
cur += 1 → cur = 5
wrong  i = 5 → nums[5] = 2 < nums[4] = 9
Sequence breaks.
max_valid = max(0, 5 // 2, min(0, 5)) → max_valid = 2
pre = 5
cur = 1


i = 6 → nums[6] = 3 > nums[5] = 2
cur += 1 → cur = 2
i = 7 → nums[7] = 4 > nums[6] = 3
cur += 1 → cur = 3

wrong i = 8 → nums[8] = 3 < nums[7] = 4
Sequence breaks again.
 max_valid = max(2, 3 // 2, min(5, 3)) → max_valid = 3
pre = 3
cur = 1

wrong i = 9 → nums[9] = 1 < nums[8] = 3 
Sequence breaks again.
 max_valid = max(3, 1 // 2, min(3, 1)) → max_valid = 3
pre = 1
cur = 1

Final Check
max_valid = max(3, 1 // 2, min(1, 1)) → still 3
return max_valid >= k → 3 >= 3 → True

'''



'''
or
'''
from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pre = 0
        cur = 1
        max_valid = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                max_valid = max(max_valid, cur // 2, min(pre, cur))
                pre = cur
                cur = 1

        # Final check for the last increasing sequence
        max_valid = max(max_valid, cur // 2, min(pre, cur))
        return max_valid >= k
