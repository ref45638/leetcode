#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head == None):
          return None

        cur = head
        result = Node(head.val, None, None)
        node = result
        m = dict()
        m[cur] = result

        cur = head.next
        while(cur != None):
          t = Node(cur.val, None, None)
          node.next = t
          m[cur] = t
          cur = cur.next
          node = node.next

        cur = head
        node = result
        while(cur != None):
          if(cur.random != None):
            node.random = m[cur.random]
          cur = cur.next
          node = node.next

        return result

# @lc code=end
