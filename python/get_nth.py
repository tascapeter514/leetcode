# Linked Lists - Get Nth

# Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on.

# So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);

# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2

# The index should be in the range [0..length-1]. If it is not, or if the list is empty, GetNth() should throw/raise an exception (ArgumentException in C#, InvalidArgumentException in PHP, Exception in Java).

class Node(object):
#     """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


test0 = {
    'input': {
        'linked_list': Node(1, Node(2, Node(3, None))),
        'idx': 0
    },
    'output': 1
}

test1 = {
    'input': {
        'linked_list': Node(42, Node(13, Node(666, None))),
        'idx': 1
    },
    'output': 13
}

test2 = {
    'input': {
        'linked_list': Node(1, Node(2, Node(3, None))),
        'idx': 1
    },
    'output': 2

}

tests = [test0, test1,test2]




def get_nth(node, index):
    count = 0
    print('idx:', index)
    while count < index:
        print('curr node:', node.data)
        node = node.next
        count += 1
    print('nth node:', node.data)
    return node.data
        
    # Your code goes here.

print(get_nth(test0['input']['linked_list'], test0['input']['idx']))

for test in tests:
    print(get_nth(test['input']['linked_list'], test['input']['idx']) == test['output'])


