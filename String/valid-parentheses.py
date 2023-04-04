class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {"(": ")", "[": "]", "{": "}"}
        
        for bracket in s:
            if bracket in brackets_map.keys():
                # if opening bracket, push it onto the stack
                stack.append(bracket)
            elif stack and brackets_map[stack[-1]] == bracket:
                # if closing bracket matches the most recent opening bracket, pop it off the stack
                stack.pop()
            else:
                # invalid sequence
                return False
        
        # if the stack is empty, the sequence is valid
        return not stack