# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {repr(self.next)})"
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        pass

def build_list(list = []):
    if not list: return None
    dummy = ListNode(0)
    curr = dummy
    for el in list:
        print(el)
        print('curr:', curr)
        node = ListNode(el)
        curr.next = node
        curr = curr.next
    return dummy.next

    
        

result = build_list([1, 2])

print('result:', result)