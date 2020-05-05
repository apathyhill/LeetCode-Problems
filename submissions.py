"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    substr = "" # Keep track of substring
    len_substr = 0 # Leep length
    for char in s: # Loop through string
        if char in substr: # If character in substring
            ind = substr.index(char) 
            if len(substr) > len_substr: # Check if it's longer, and set to longest if True
                len_substr = len(substr)
            ind = substr.index(char) 
            substr = substr[ind+1:] # Delete the characters of the substring up to the first occurance of the current character
        substr += char # Add character to substring
    if len(substr) > len_substr: # One last check when the loop ends
        len_substr = len(substr)
    return len_substr # Return length

"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
def longestPalindrome(self, s: str) -> str:
    longest_substr = ""
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                if len(substr) > len(longest_substr):
                    longest_substr = substr
    return longest_substr

"""
https://leetcode.com/problems/reverse-integer/
"""
def reverse(self, x: int) -> int:
    if x >= 0:
        num = int(str(x)[::-1])
    else:
        num = -int(str(x)[1:][::-1])
    if num > 2**31-1 or num < -(2**31):
        return 0
    return num

"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
def myAtoi(self, s: str) -> int:
    s = s.strip()
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        elif char in "+-":
            if num_str == "":
                num_str += char
            else:
                break
        else:
            break
    if num_str in ["", "-", "+"]:
        return 0
    num = max(min(int(num_str), 2**31-1), -(2**31))
    return num

"""
https://leetcode.com/problems/palindrome-number/
"""
def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]

"""
https://leetcode.com/problems/integer-to-roman/
"""
def intToRoman(self, num: int) -> str:
    s = ""
    values = {("M", 1000), 
                ("D", 500), 
                ("C", 100), 
                ("L", 50), 
                ("X", 10), 
                ("V", 5), 
                ("I", 1)}
    
    for i in range(0, len(values), 2):
        v = values[i]
        div = num // v[1]
        if div > 0:
            if div % 5 == 4:
                s += values[i][0]
            if (div+1) // 5 == 1:
                s += values[i-1][0] 
            elif (div+1) // 5 == 2:
                s += values[i-2][0] 
            if div % 5 < 4:
                s += values[i][0] * (div % 5)
            num -= v[1] * div
    return s

"""
https://leetcode.com/problems/roman-to-integer/
"""
def romanToInt(self, s: str) -> int:
    values = {"M": 1000, 
                "D": 500,
                "C": 100, 
                "L": 50, 
                "X": 10, 
                "V": 5, 
                "I": 1}
    num = 0
    before_check = 0
    for i, char in enumerate(s):
        if i < len(s) - 1:
            if values[s[i+1]] > values[char]:
                before_check = -values[char]
                continue
        num += before_check + values[char]
        before_check = 0
    return num

"""
https://leetcode.com/problems/longest-common-prefix/
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    
    prefix = sorted(strs, key=lambda x: len(x))[0]
    while not prefix == "":
        is_valid = True
        for s in strs:
            if not s.startswith(prefix):
                is_valid = False
                break
        if is_valid:
            break
        else:
            prefix = prefix[:-1]
    return prefix

"""
https://leetcode.com/problems/valid-parentheses/
"""
def isValid(self, s: str) -> bool:
    brackets = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
    }
    
    stack = ""
    for char in s:
        if char in brackets:
            stack += char
        else:
            if len(stack) == 0:
                return False
            if brackets[stack[-1]] == char:
                stack = stack[:-1]
            else:
                return False
    if len(stack) == 0:
        return True