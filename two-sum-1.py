class Solution(object):
   
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cloneArr = sorted(nums)
        sum = 0
        rightPointer = len(nums) - 1
        rightPointerValue = nums[rightPointer]
        leftPointer = 0
        leftPointerValue = nums[0]
        print(len(nums))
        for i in range(1, len(nums)):
            print("rightPointer:", rightPointer)
            print("rightPointerValue:", rightPointerValue)
            print("leftPointer:", leftPointer)
            print("leftPointerValue:", leftPointerValue)
            
            if rightPointerValue + leftPointerValue == target:
                sum = rightPointerValue + leftPointerValue
                print(sum)
                return [rightPointer, leftPointer]
        
            if rightPointerValue + leftPointerValue > target:
                rightPointer -= 1
                rightPointerValue = cloneArr[rightPointer]

            if rightPointerValue + leftPointerValue < target:
                leftPointer += 1
                leftPointerValue = cloneArr[leftPointer]



    def twoSum2(nums, target):
        
        if len(nums) == 1:
            return "[0]"
        
        rightPointerIndex = len(nums) % 2 + 1
        rightPointerValue = nums[len(nums) % 2 + 1]
        leftPointerIndex = ( len(nums) % 2 ) 
        leftPointerValue = nums[( len(nums) % 2 )]
        
        for i in range(1, len(nums)):
            
            print("rightPointer Index:", rightPointerIndex)
            print("rightPointerValue:", rightPointerValue)
            print("leftPointer Index:", leftPointerIndex)
            print("leftPointerValue:", leftPointerValue)
            
            if rightPointerValue + leftPointerValue == target:
                return [rightPointerIndex, leftPointerIndex]
            
            if rightPointerValue + leftPointerValue > target:
                rightPointerIndex -= 1
                rightPointerValue = nums[rightPointerIndex]
                
            if rightPointerValue + leftPointerValue < target:
                leftPointerIndex += 1
                leftPointerValue = nums[leftPointerIndex]
            
        
        
print(Solution.twoSum2([3,2,3], 6))




