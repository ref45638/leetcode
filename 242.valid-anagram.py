#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False

      m = dict()
      for i in range(len(s)):
        if m.get(s[i]) == None:
          m[s[i]] = 1
        else:
          m[s[i]] += 1
        if m.get(t[i]) == None:
          m[t[i]] = -1
        else:
          m[t[i]] += -1
          
      for c in m:
        if m[c] != 0:
          return False
      
          
      return True
        
# @lc code=end

