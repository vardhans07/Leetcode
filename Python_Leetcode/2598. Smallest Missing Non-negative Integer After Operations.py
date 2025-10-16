'''

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 105
-109 <= nums[i] <= 109


'''


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = Counter(num % value for num in nums)
        mex = 0

        while True:
            r = mex % value
            if freq[r] > 0:
                freq[r] -= 1                    #supose freq = {2: 1} then freq [2] is 1 thats why here 1-1 is 0 
                mex += 1
            else:
                return mex
'''
Input: nums = [1,-10,7,13,6,8], value = 5

Remainders: [1, 0, 2, 3, 1, 3]
Frequencies: {1: 2, 0: 1, 2: 1, 3: 2}  then ------------------>> means following is same for better understanding we take this as sorted 
freq = {
    0: 1,  # only -10 gives remainder 0
    1: 2,  # from 1 and 6
    2: 1,  # from 7
    3: 2   # from 13 and 8
}

Try to build:

0 -> 0 % 5 = 0 -> freq[0] = 1 -> OK

1 -> 1 % 5 = 1 -> freq[1] = 2 -> OK

2 -> 2 % 5 = 2 -> freq[2] = 1 -> OK

3 -> 3 % 5 = 3 -> freq[3] = 2 -> OK

4 -> 4 % 5 = 4 -> freq[4] = 0 -> STOP

Output: 4

'''





