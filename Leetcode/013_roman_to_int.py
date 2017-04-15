def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num, prev = 0, 1000
    
    for c in s:
        num, prev = num + map[c] - 2*prev if map[c] > prev else num + map[c], map[c]
        
    return num
