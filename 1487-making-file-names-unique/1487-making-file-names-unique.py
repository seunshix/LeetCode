class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d, res = {}, []
        for name in names:
            if name in d:
                orig_name = name
                # get the smallest positive key
                key = d[name]
                while(name in d):
                    name = orig_name + "({})".format(key)
                    key += 1
                d[name] = 1
				# memoization done so as to get the latest version of this next time
                d[orig_name] = key
            else:
                d[name] = 1
            res.append(name)
        return res
        