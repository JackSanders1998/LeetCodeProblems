class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest_word = 100
        for word in strs:
            if len(word) < shortest_word:
                shortest_word = len(word)
        if shortest_word == 0:
            return ""
        prefix = ""
        for x in range(shortest_word):
            row_prefix = strs[0][x]
            for y in range(len(strs)):
                if strs[y][x] == row_prefix:
                    row_prefix = strs[y][x]
                elif strs[y][x] != row_prefix:
                    return prefix
            prefix += row_prefix
        return prefix
                        
            
