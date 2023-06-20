class Solution(object):
    def longestCommonPrefix(self, strs):
        first = strs[0]
        pref = ""
        temp = ""
        true = True
        for x in range(0, len(first)+1):
            temp = first[:x]
            for y in range(1, len(strs)):
                if temp not in str(strs[y][:len(temp)]):
                    true = False
            if true:
                pref = temp
            else:
                break
        if len(strs) == 1:
            return strs[0]
        return pref
