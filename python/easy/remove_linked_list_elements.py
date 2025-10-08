# 203. Remove Linked List Elements
# Easy
# Topics
# premium lock iconCompanies

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:

# Input: head = [], val = 1
# Output: []

# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

# Definition for singly-linked list.

class Solution(object):
    def removeElements(self, head, val):
        pass
       


from utils.classes import LinkedList, Node
from utils.tests import Test

list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()

output1 = LinkedList()
output2 = LinkedList()
output3 = LinkedList()

list1_values = [1,2,6,3,4,5,6]
list2_values = []
list3_values = [7,7,7,7]

output1_values = [1,2,3,4,5]
output2_values = []
output3_values = []

for el in list1_values:
    node = Node(el)
    list1.append(el)

for el in list2_values:
    node = Node(el)
    list2.append(el)

for el in list3_values:
    node = Node(el)
    list3.append(el)

for el in output1_values:
    node = Node(el)
    output1.append(node)

for el in output2_values:
    node = Node(el)
    output2.append(node)

for el in output3_values:
    node = Node(el)
    output3.append(node)

test1 = Test({'head': list1, 'val': 6}, output1)
test2 = Test({'head': list2, 'val': 1}, output2)
test3 = Test({'head': list3, 'val': 7}, output3)

tests = [test1, test2, test3]

solution = Solution()

for test in tests:
    print(solution.removeElements(**test.input) == test.output)




        




