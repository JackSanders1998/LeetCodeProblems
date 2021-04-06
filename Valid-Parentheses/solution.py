class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            "(": {"pos": "open", "opp": ")"},
            ")": {"pos": "closed", "opp": "("},
            "[": {"pos": "open", "opp": "]"},
            "]": {"pos": "closed", "opp": "["},
            "{": {"type": "curly", "pos": "open", "opp": "}"},
            "}": {"type": "curly", "pos": "closed", "opp": "{"}
        }
        if len(s) % 2 != 0:
            return False
        opened = 0
        closed = 0
        stack = []
        for i in range(len(s)):
            # print(stack, s[i])
            if paren_dict[s[i]]["pos"] == "open":
                opened += 1
                stack.append(s[i])
            else:
                closed += 1
                try:
                    if paren_dict[stack.pop()]["opp"] != s[i]:
                        return False
                except:
                    return False
        if closed == opened:
            return True
        else:
            return False
            
            
