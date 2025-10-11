'''
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109
'''




class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        
        # Count frequency of each damage
        freq_map = {}
        for p in power:
            freq_map[p] = freq_map.get(p, 0) + 1
        
        unique = sorted(freq_map.keys())
        n = len(unique)
        
        # Find for each unique damage the next index where damage > current + 2
        def next_index(i):
            target = unique[i] + 3
            # Linear search (binary search not used since no imports allowed)
            for j in range(i+1, n):
                if unique[j] >= target:
                    return j
            return n 
        
        dp = [0] * (n + 1)
        
        for i in range(n-1, -1, -1):
            skip = dp[i+1]
            take = unique[i] * freq_map[unique[i]]
            nxt = next_index(i)
            if nxt < n:
                take += dp[nxt]
            dp[i] = max(skip, take)
        
        return dp[0]


'''
or
'''

from typing import List
from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        n = len(power)
        
        # Count frequency of each damage value
        freq = Counter(power)
        unique = sorted(freq.keys())
        
        # Build an array to store the next valid index for each unique damage
        nxt = [0] * len(unique)
        
        # For each damage, find the first damage > curr + 2 using binary search
        for i, val in enumerate(unique):
            nxt[i] = bisect.bisect_right(unique, val + 2)
        
        # DP array
        dp = [0] * (len(unique) + 1)
        
        # Bottom-up DP. dp[i] = max total damage using unique damages from i-th to end
        # Start from last unique damage backwards
        for i in range(len(unique) - 1, -1, -1):
            # Option 1: skip current damage
            skip = dp[i + 1]
            # Option 2: take all spells of current damage + dp[next valid damage]
            take = unique[i] * freq[unique[i]] + dp[nxt[i]]
            dp[i] = max(skip, take)
        
        return dp[0]
