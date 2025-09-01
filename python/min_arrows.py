# 452. Minimum Number of Arrows to Burst Balloons

# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

test_one = {
    'input': {
        'points': [[10,16],[2,8],[1,6],[7,12]]
    },
    'output': 2
}

test_two = {
    'input': {
        'points': [[1,2],[3,4],[5,6],[7,8]]
    },
    'output': 4
}

test_three = {
    'input': {
        'points': [[1,2],[2,3],[3,4],[4,5]]
    },
    'output': 2
}

tests = [test_one, test_two, test_three]

class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points)
        print(points)
        for left_index in range(len(points) -1):
            left_point = points[left_index]
            right_point = points[left_index + 1]
            left_point_last_element = left_point[len(left_point) - 1]
            right_point_first_element = right_point[0]
            if left_point_last_element < right_point_first_element:
                continue
            else:
                new_array = left_point + right_point
                print(new_array)

            
           

            
                

            
                

            



Sol = Solution()

print(Sol.findMinArrowShots(test_one['input']['points']))
print(Sol.findMinArrowShots(test_one['input']['points']) == test_one['output'])
print(Sol.findMinArrowShots(test_two['input']['points']) == test_two['output'])
print(Sol.findMinArrowShots(test_three['input']['points']) == test_three['output'])
