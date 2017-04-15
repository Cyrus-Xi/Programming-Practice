def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    map = {'(': ')', '{': '}', '[': ']'}
    stack = []
    
    for i, c in enumerate(s):
        if c in map: 
            stack.append(c)
        elif c in map.values(): 
            # Also fails if stack is empty -> too many closing parens.
            if not stack or map[stack.pop()] != c: return False

    return not stack
