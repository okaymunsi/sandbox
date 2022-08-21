"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.


Example 2:
Input: nums = [1]
Output: 1


in = [1,1,1,1,-1,3,-4] --> [1,1,1,1,-1,3]
in = [1,1,1,1,-4,3,-1] --> [1,1,1,1]
in = [-2,1,1,1,-1,3,-4] --> [1,1,1,-1,3] --> [3,-1,3] --> [2,3]
in = [-2,1,1,1,-1,3,-4] --> [-2,3,-1,3,-4]

nums = [5,4,-1,7,8] --> [9,-1,15]
nums = [5,4,-9,15] --> [9,-9,15]
nums = [5,4,-10,15] --> [15]

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Example 4:
[9,-1,15] --> [9, -1, 15]
[9,-10,15] --> [15]

[5,4,-10,7,8]

"""

def maxSubarray(nums):
    local_max = {}
    start = 0
    while(start < len(nums)):
        number = nums[start]
        if number < 0:
            start += 1
            continue

        sum = number
        for j in range(start + 1, len(nums)):
            old_sum = sum
            sum = sum + nums[j]
            
            if j < 0:
                local_max[old_sum] = (start, j - 1)
                if sum < 0:
                    start = j + 1
                    break

            #if sum < 0:
            #    local_max[old_sum] = (start, j - 1)
            #    start = j + 1
            #    break
            #elif j == len(nums) - 1:
            #    local_max[sum] = (start, j)
            #    start = j + 1

    global_max = max(local_max.keys())
    begin, end = local_max[global_max]
    return nums[begin:end+1], local_max

for test in [[5,4,-1,7,8], [-2,1,-3,4,-1,2,1,-5,4], [1,1,1,1,-1,3,-4], [-4,-3,4,-2,-1,-4,-1]]:
    print(f'Test "{test}":')
    answer, local_max = maxSubarray(test)
    print(answer)
    print(local_max)
    print()