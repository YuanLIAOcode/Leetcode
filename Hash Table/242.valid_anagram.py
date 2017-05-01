class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dir, t_dir = {}, {}
        for char in s:
            s_dir[char] = s_dir.get(char, 0) + 1
        for char in t:
            t_dir[char] = t_dir.get(char, 0) + 1
        return s_dir == t_dir