# 179. Largest Number


# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"

# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

 

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 109

testOne = {
    'input': {
        'nums': [10, 2]
    },
    'output': '210'
}

testTwo = {
    'input': {
        'nums': [3,30,34,5,9]
    },
    'output': '9534330'
}

class Solution(object):
    def largestNumber(self, nums):
        start = 0
        end = len(nums)  - 1
        forward = str(nums[start]) + str(nums[end])
        reverse = str(nums[end]) + str(nums[start])
        if (int(forward) > int(reverse)):
            print(int(forward))
        else:
            print(int(reverse))

        # if str(nums[start]) + str(nums[end]) > str(nums[end]) + str(nums[start]):
            
        # if str(nums[start]) + str(nums(end)) > str(nums[end]) + str(nums[start]):
        #     print(str(nums[start]) + str(nums(end)))
        # else:
        #     print(str(nums[end]) + str(nums[start]))
        

            

            
            # if len(str(nums[start])) > 1:
            #     str(nums[start])[0:1]
            #     print()
            # start += 1
            # end -= 1
            # if len(str(num)) > 1: print(str(num)[0])
            # else: print(num) 

Sol = Solution()


print(Sol.largestNumber(testOne['input']['nums']) == testOne['output'])
print(Sol.largestNumber(testTwo['input']['nums']) == testTwo['output'])
print(Sol.largestNumber(testTwo['input']['nums']))

