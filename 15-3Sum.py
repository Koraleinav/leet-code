"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first way - two pointers with a sorted array
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: # how we skip duplicates for the first element
                continue
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[right] + nums[left]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else: 
                    res.append([nums[i], nums[right], nums[left]])    
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # how we skip duplicates for the left element
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # how we skip duplicates for the right element
                        right -= 1
        return res

        """

        # second way - dividint the array into 3 :
        # negetive , positive and zeros
        neg, pos, res = [], [], set()
        zeros = 0

        for num in nums: 
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zeros += 1
        
        # if we have one zero, it means that there is a possible solution of [-n, 0, n]
        # if we have 3 zeros, it means that there is a possible solution of [0, 0, 0]
        if zeros:
            for n in neg:
                if -n in pos:
                    res.add(tuple(sorted([-n, 0, n])))  # add sorted triplet to the set
            if zeros > 2:
                res.add((0, 0, 0))
        

        # for all the pairs of negetive numbers, check to see if the complementary exists in the positive array
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -(neg[i] + neg[j])
                if target in pos:
                    res.add(tuple(sorted([neg[i], neg[j], target])))  # add sorted triplet to the set
        
        # for all the pairs of positive numbers, check to see if the complementary exists in the negative array
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -(pos[i] + pos[j])
                if target in neg:
                    res.add(tuple(sorted([pos[i], pos[j], target])))  # add sorted triplet to the set
        
        return [list(triplet) for triplet in res] # for the array return type ( set -> array)

        
        
