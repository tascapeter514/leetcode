# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {repr(self.next)})"

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2: return list1
        if not list1 or not list2: return list1 or list2
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        print('curr:', curr)
        print('dummy:', dummy)
            
            
        




                

                
        

            



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
    if not list: return None
    curr = ListNode(list[0])
    curr.next = build_list_recurse(list[1:])
    return curr


list1 = build_list([1, 2, 4])

list2 = build_list_recurse([1, 3, 4])

solution = Solution()
print('solution:', solution.mergeTwoLists(list1, list2))