"""
A problem from K*******s coding assessment.
"""


class Solution:
    def is_valid(self, s: str):

        if len(s) % 2 != 0:
            return False

        b1 = ['(', ')']
        b2 = ['[', ']']
        b3 = ['{', '}']
        proc_stack = list()

        for c in s:
            if c in list(b1[0] + b2[0] + b3[0]):
                proc_stack.insert(0, c)
                # print(f"stack={proc_stack}")
            elif c in list(b1[1] + b2[1] + b3[1]):
                if len(proc_stack) == 0:
                    return False
                temp = [proc_stack[0], c]
                # print(f"temp list now is {temp}")
                if temp != b1 and temp != b2 and temp != b3:
                    # print("Not valid.")
                    return False
                else:
                    del proc_stack[0]
                    # print(f"stack={proc_stack}")
            else:
                continue
        if len(proc_stack) != 0:
            return False
        return True
