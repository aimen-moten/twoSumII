# Leetcode 167: Two Sum II in Sorted Array

# Algorithm:
# Set two pointers, i and j to the start and end values in the array
# Compute the current sum using nums[i] and nums[j]
# If current Sum is greater than our target, we move j to the left: this is because the array is sorted and we know that we need to decrement our sum by some value to get to our target.
# Similarly, if current sum is lower than our target then we move i to the right because we know that we need to increment the sum by a certain value to reach our target.
# Finally, if neither of the above are the case, then it means that the current sum is equal to the target and we can return i+1 and j+1 to give the index of the values (+1 because it is a 1-indexed array)

#Code:

def twoSumII(nums: list[int], target: int):
    i = 0
    j = len(nums)-1
    currSum = 0
    while i < j:
        currSum = nums[i] + nums[j]
        if currSum > target:
            j = j - 1
        elif currSum < target:
            i = i + 1
        else:
            return [i+1, j+1]
        
# To Test:
print(twoSumII([2,7,11,15], 9))
print(twoSumII([2,7,11,15], 18))
print(twoSumII([2,3,4], 6))
print(twoSumII([-1,0], -1))
