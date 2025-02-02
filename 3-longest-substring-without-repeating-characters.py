"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
"""

        
# firstly you check if the previous char of s is the dame as the current one 
# then we check if the letter is relevent to our string, so we check if the char
# is already at our demoString
# then we check that i is not 0 so we could manipulate the string
# and lastley we check that i is not larger then the length of demoString

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        demoString = ""
        maxLength = 0
        for i in range(len(s)):
            if s[i] not in demoString:
                demoString += s[i]
                # remove everything up to (and including) first occurrence of s[i]
            else:
                index = demoString.index(s[i])
                demoString = demoString[index + 1:] + s[i] 

            maxLength = max(maxLength, len(demoString))
        return maxLength
    
#second solution:
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        charIndex = {}  # Dictionary to store the last index of each character
        left = 0  # Left boundary of the current substring
        maxLength = 0  # Maximum length of a unique substring

        for right in range(len(s)):
            if s[right] in charIndex and charIndex[s[right]] >= left:
                # Move 'left' to exclude the previous occurrence of s[right]
                left = charIndex[s[right]] + 1

            # Store/update the last seen index of s[right]
            charIndex[s[right]] = right
            
            # Update max length of the substring
            maxLength = max(maxLength, right - left + 1)

        return maxLength