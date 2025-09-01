# 316. Remove Duplicate Letters
# Medium
# Topics
# premium lock iconCompanies
# Hint

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is

# among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"

# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

test_one = {
    'input': {
        's': 'bcabc'
    },
    'output': 'abc'
}

test_two = {

    'input': {
        's': 'cbacdcbc'
    },
    'output': 'acdb'
}

tests = []
tests.append(test_one)
tests.append(test_two)

class Solution(object):
    def removeDuplicateLetters(self, s):
        last_pos = {string: s.rindex(string) for string in s}
        string_builder = []
        seen = set()
        for i, char in enumerate(s):
            print('string builder:', string_builder)
            print('seen:', seen)
            if char not in seen:
                while string_builder and char < string_builder[-1] and i < last_pos[string_builder[-1]]:
                    print(f'discarding char {char}')
                    seen.discard(string_builder.pop())
                print(f'adding char {char}')
                seen.add(char)
                string_builder.append(char)


        
        
            


                
        
                
        
            
        
Sol = Solution()

print(Sol.removeDuplicateLetters(test_one['input']['s']))

for test in tests:
    print(Sol.removeDuplicateLetters(test['input']['s']) == test['output'])