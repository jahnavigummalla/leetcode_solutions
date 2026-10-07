class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        # Find minimum removals needed
        level = {s}

        while level:
            valid = []

            for string in level:
                if isValid(string):
                    valid.append(string)

            if valid:
                return valid

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    # Only remove parentheses
                    if string[i] == '(' or string[i] == ')':
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            level = next_level

        return [""]