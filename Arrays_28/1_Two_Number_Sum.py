# Solution1 :
# O(n^2) time | O(1) space
def twoNumberSumSolution1(array, targetSum):
    for idx1, num1 in enumerate(array):
        for idx2, num2 in enumerate(array):
            if idx1 != idx2:
                if num1 + num2 == targetSum:
                    return [num1, num2]
    return []

# Solution2 :
# O(n) time | O(n) space
def twoNumberSumSolution2(array, targetSum):
    nums = {}
    for num in array:
        match = targetSum - num
        if match in nums:
            return [match, num]
        else:
            nums[num] = True
    return []

# Solution3:
# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left_idx = 0
    right_idx = len(array)-1
    while left_idx < right_idx:
        currentSum = array[left_idx] + array[right_idx]
        if currentSum == targetSum:
            return [array[left_idx], array[right_idx]]
        elif currentSum < targetSum:
            left_idx += 1
        elif currentSum > targetSum:
            right_idx -= 1
    return []
