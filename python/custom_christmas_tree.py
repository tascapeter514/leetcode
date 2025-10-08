# Custom Christmas Tree
# 682894% of 255408 of 1,041myjinxin2015

#     Python
#     3.11

#         VIM
#         EMACS

# Instructions
# Output
# Task

# Christmas is coming, and your task is to build a custom Christmas tree with the specified characters and the specified height.
# Inputs:

#     chars: the specified characters.
#     n: the specified height. A positive integer greater than 2.

# Output:

#     A multiline string. Each line is separated by \n. A tree contains two parts: leaves and trunks.

# The leaves should be n rows. The first row fill in 1 char, the second row fill in 3 chars, and so on. A single space will be added between two adjust chars, and some of the necessary spaces will be added to the left side, to keep the shape of the tree. No space need to be added to the right side.

# The trunk should be at least 1 unit height, it depends on the value of the n. The minimum value of n is 3, and the height of the tree trunk is 1 unit height. If n increased by 3, and the tree trunk increased by 1 unit. For example, when n is 3,4 or 5, trunk should be 1 row; when n is 6,7 or 8, trunk should be 2 row; and so on.

# Still not understand the task? Look at the following example ;-)
# Examples

# For chars = "*@o" and n = 3,the output should be:

#   *
#  @ o
# * @ o
#   |



# For chars = "*@o" and n = 6,the output should be:

#      *
#     @ o
#    * @ o
#   * @ o *
#  @ o * @ o
# * @ o * @ o
#      |
#      |

# For chars = "1234" and n = 6,the output should be:

#      1
#     2 3
#    4 1 2
#   3 4 1 2
#  3 4 1 2 3
# 4 1 2 3 4 1
#      |
#      |

# For chars = "123456789" and n = 3,the output should be:

#   1
#  2 3
# 4 5 6
#   |

from itertools import cycle, islice

test0 = {
    'input': {
        'chars': '*@o',
        'n': 3
    },
    'output': """ 
     *
    @ o
   * @ o
     |"""
}

test1 = {
    'input': {
        'chars': '*@o',
        'n': 6
    },
    'output': """
     *
    @ o
   * @ o
  * @ o *
 @ o * @ o
* @ o * @ o
     |
     |"""
}

test2 = {
    'input': {
        'chars': '1234',
        'n': 6
    },
    'output': """
  1
 2 3
4 5 6
  |"""
}

tests = [test0, test1, test2]

def custom_christmas_tree(chars, n):
    leaves = cycle(chars)

    margin = lambda i: (n - i) * '#'
    branch = lambda i: "$".join(islice(leaves, i))
    line = lambda i: margin(i) + branch(i)
    body = list(map(line, range(1, n + 1)))
    trunk = [margin(1) + "|"] * (n//3)
    return '\n'.join(body + trunk)

    
    

    

    
    
        


print(custom_christmas_tree(test1['input']['chars'], test0['input']['n']))

# for test in tests:
#     print(custom_christmas_tree(test['input']['chars'], test['input']['n']) == test['output'])