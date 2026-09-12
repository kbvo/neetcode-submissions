class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {"]" : "[", ")" : "(", "}" : "{"}
        stack = []
        for p in s:
            if p in parDict:
                if stack and stack[-1] == parDict[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not stack
             