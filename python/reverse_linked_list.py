# 206. Reverse Linked List
# Easy
# Topics
# premium lock iconCompanies

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1, l2 = l1.next, l2.next
    return l1 is None and l2 is None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

test0 = {
    'input': {
        'head': ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    },
    'output': ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None)))))
}

test1 = {
    'input': {
        'head': ListNode(1, ListNode(2, None))
    },
    'output': ListNode(2, ListNode(1, None))
}

test2 = {
    'input': {
        'head': ListNode(None)
    },
    'output': ListNode(None)
}

tests = [test0, test1, test2]

class Solution(object):



    def reverseList(self, head):
        result_head = ListNode(None)

        while head != None:
            print(head.val)
            result_head = ListNode(head.val, result_head)
            head = head.next
        print("result head:", result_head.val)
        return result_head

Sol = Solution()

result_head = Sol.reverseList(test0['input']['head'])

print(result_head)



for test in tests:
    if compare_linked_lists(result_head, test['output']):
        print('passed')
    else:
        print('Failed')