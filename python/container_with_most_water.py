# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

testOne = {
    'input': {

        'height': [1,8,6,2,5,4,8,3,7]

    },

    'output': 49
}

testTwo = {
    'input': {
        'height': [1,1]
    },

    'output': 1
}

# class Solution(object):
#     def maxArea(self, height):
#         res = 0
#         left, right = 0, len(height) -1
#         while left < right:
#             area = (right - left) * min(height[left], height[right])
#             res = max(res, area)
#             print(res)
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
            
#         return res

class Solution(object):
    def maxArea(self, height):
        res = 0
        left = 0
        for right in range(1, len(height)):
            print('left height:', height[left])
            print('right height:', height[right])
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            
        return res

        
            
            

        


        
        


Sol = Solution()
print(Sol.maxArea(testOne['input']['height']))
# print(Sol.maxArea(testOne['input']) == testOne['output'])
# print(Sol.maxArea(testTwo['input']) == testTwo['output'])
