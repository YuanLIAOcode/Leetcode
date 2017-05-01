class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dir, t_dir = {}, {}
        for key, value in enumerate(s):
            s_dir[value] = s_dir.get(value, []) + [key]
        for key, value in enumerate(t):
            t_dir[value] = t_dir.get(value, []) + [key]

        print(s.find)

        print(sorted(s_dir.values()) == sorted(t_dir.values()))

        # return map(s.find, s) == map(t.find, t)


solution = Solution()
solution.isIsomorphic("addaf", "eggee")
