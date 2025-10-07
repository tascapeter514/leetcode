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
        node = ListNode(el)
        curr.next = node
        curr = curr.next
    return dummy.next


def build_list_recurse(list = []):
    print('list:', list)
    if not list: return None
    curr = ListNode(list[0])
    print('current node:', curr)
    curr.next = build_list_recurse(list[1:])
    print('final curr:', curr)
    return curr


result = build_list([1, 2])

new_result = build_list_recurse([1, 2])

print('result:', new_result)