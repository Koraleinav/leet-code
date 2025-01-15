class Solution(object):
    """
     Works, 
        Time Complexity : o(n) - o(n^2)
    """
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    def twoSum(nums, target):

        rightPointer = len(nums) - 1
        rightPointerValue = nums[rightPointer]
        leftPointer = 0
        leftPointerValue = nums[0]
        
        
        for i in range(1, len(nums) * 2):

            if rightPointerValue + leftPointerValue == target:
                return [rightPointer, leftPointer]
        
            if rightPointerValue + leftPointerValue > target:
                rightPointer -= 1
                rightPointerValue = nums[rightPointer]

            if rightPointerValue + leftPointerValue < target:
                leftPointer += 1
                leftPointerValue = nums[leftPointer]

    """
     Works,
        Time Complexity : O(nlogn)
        
    """
    def twoSum2(nums, target):
           
        dict_with_indexs = [(num, index) for index, num in enumerate(nums)]
        dict_with_indexs.sort(key=lambda x: x[0]) # sort by the value
        
        # the dict will look like this:
        # input: [3, 2, 4] → after sorting: [(2, 1), (3, 0), (4, 2)]
        # [0] = value, [1] = index of that value in the original array
        
        for i in range(len(dict_with_indexs)):
            currentValue, currentIndex = dict_with_indexs[i]
            complement = target - currentValue
            
            left = i + 1
            right = len(dict_with_indexs) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                midValue, midIndex = dict_with_indexs[mid]
                
                if midValue == complement:
                    return [currentIndex, midIndex]
                elif midValue < complement:
                    left = mid + 1
                else:
                    right = mid -1
                    
        return None
            
        
        
        
        
        
print(Solution.twoSum2([2, 7, 11, 15], 9))  # Output: [0, 1]
print(Solution.twoSum2([3, 2, 4], 6))       # Output: [1, 2]
print(Solution.twoSum2([3, 3], 6))          # Output: [0, 1]
print(Solution.twoSum2([3,0,1,1,1], 3))




