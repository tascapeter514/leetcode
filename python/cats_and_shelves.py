# Description

# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:

#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐       
# │------5-│        
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │     
# BANG!────┘  ├─────► OK! 
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘

# Input

# Start and finish shelf numbers (always positive integers, finish no smaller than start)
# Task

# Find the minimum number of jumps to go from start to finish
# Example

# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

test0 = {
    'input': {
        'start': 1,
        'finish': 5
    },
    'output': 2
}

test1 = {
    'input': {
        'start': 3,
        'finish': 10
    },
    'output': 3
}

test2 = {
    'input': {
        'start': 0,
        'finish': 2
    },
    'output': 2

}

# def solution(start, finish):
#     steps = 0
#     remainder = finish - start
#     while 0 < remainder:
#         print(f'{steps} steps taken, {remainder} steps left')
#         if remainder >= 3:
#             steps += 1
#             remainder -= 3
#         else:
#             steps += 1
#             remainder -=1
#     return steps
    
def solution(start, finish):
    n = finish -start
    return n // 3 + n % 3



tests = [test0, test1, test2]

print(solution(test0['input']['start'], test0['input']['finish']))

for test in tests:
    print(solution(test['input']['start'], test['input']['finish']) == test['output'])