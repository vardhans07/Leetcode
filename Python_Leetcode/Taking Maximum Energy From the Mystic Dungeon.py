'''
In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.

 

Example 1:

Input: energy = [5,2,-10,-5,1], k = 3

Output: 3

Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:

Input: energy = [-2,-3,-1], k = 2

Output: -1

Explanation: We can gain a total energy of -1 by starting from magician 2.

 

Constraints:

1 <= energy.length <= 105
-1000 <= energy[i] <= 1000
1 <= k <= energy.length - 1

'''


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:]  # here you can see [:], you get a separate copy.  thats mean dp is a new list with the same values as original(energy).
        n = len(energy) # lenght of energy 
        for i in range(n - 1 - k, -1, -1):    #range(start, stop, step)  here Step by -1 (step) → move one index backward each time
            dp[i] += dp[i + k]
        return max(dp)




'''
or 
'''

from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [None] * n  # to memoize computed sums

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if dp[i] is not None:
                return dp[i]
            dp[i] = energy[i] + dfs(i + k)
            return dp[i]

        max_gain = float('-inf')
        for start in range(n):
            max_gain = max(max_gain, dfs(start))
        return max_gain


