import re

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        good_word = []
        for word in words:
            complied_pattern = re.compile('(?i)[qwertyuiop]*$|[asdfghjkl]*$|[zxcvbnm]*$')
            if complied_pattern.match(word):
                good = complied_pattern.match(word).group(0)
                good_word.append(good)
        return good_word


solution = Solution()
solution.findWords(["Hello", "Alaska", "Dad", "Peace"])


