'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


from typing import List

 class solution :
     def twosum(self , nums : List [int] ,target :int )-> List [int]:
	       num_map ={}
		      for i , num in enumerate (nums):           #i = 0, num = 2   next  i = 1, num = 7
		         complement =traget- num                    #first checked complement = 9 - 2 = 7  then  next   complement = 9 - 7 = 2 
		         if complement in num_map:                  #7 is not in   next checked 2 is in num_map
		           return [num_map[complement], i]            #Match found!        Return [num_map[2], 1] → [0, 1]
		         num_map[num]=i                               #num_map = {2: 0}
'''

nums = [10, 20, 30]
for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")


Output:

Index: 0, Value: 10
Index: 1, Value: 20
Index: 2, Value: 30
'''

#nums is your list of integers.
# enumerate(nums) returns pairs: each pair contains the index and the value at that index.
#i is the index (position in the list).
#num is the actual number at that position.




        

