class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize
        b = "[]"
        p = "()"
        c = "{}"
        len_s = len(s)
        s_sub = s
        # # Check pairing
        # lb = s.count("[")
        # rb = s.count("]")
        # lp = s.count("(")
        # rp = s.count(")")
        # lc = s.count("{")
        # rc = s.count("}")
        # if lb!=rb:
        #     s_bool = False
        # elif lp!=rp:
        #     s_bool = False
        # elif lc!=rc:
        #     s_bool = False
        # else:
        # Remove the innermost parenthesis
        s_bool = True
        while len(s_sub) > 0:
            s_new = (s_sub
                     .replace(b,"")
                     .replace(p,"")
                     .replace(c,""))
            if s_new == s_sub:
                s_bool = False
                break
            s_sub = s_new
        return s_bool