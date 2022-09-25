'''
Solution to the problem Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       """Return all the combination of n parenthesis."""
       def generate(p, left, right):
            """Inline generator"""
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p+'(',left-1, right): yield q
                for q in generate(p+')', left, right-1):yield q
       return list(generate("", n, n))

print(Solution().generateParenthesis(3))