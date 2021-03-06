"""
520. Detect Capital
https://leetcode.com/problems/detect-capital/

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    - All letters in this word are capitals, like "USA".
    - All letters in this word are not capitals, like "leetcode".
    - Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. 

Example 1:

    Input: "USA"
    Output: True

Example 2:

    Input: "FlaG"
    Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
import doctest
import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.match(r"^[A-Z]+$", word):  # WORD
            return True
        elif re.match(r"[a-z]*$", word):  # word
            return True
        elif re.match(r"^[A-Z]", word[0:]) and re.match(
            r"[a-z]*$", str(word[1:])
        ):  # Word
            return True
        return False


def test():
    s = Solution()
    assert s.detectCapitalUse("USA") == True
    assert s.detectCapitalUse("FlaG") == False
