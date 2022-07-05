class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lst = []
        res = []
        n = 0
        for w in words:
            while len(w) + n + len(lst) > maxWidth:
                gaps = len(lst) - 1 or 1
                quotient, remainder = divmod(maxWidth - n, gaps)
                for i in range(gaps):
                    lst[i] += " " * quotient + (" " if i < remainder else "")
                res.append("".join(lst))
                n,lst = 0, []
            lst.append(w)
            n+=len(w)
        return res+[" ".join(lst).ljust(maxWidth)] if lst else []