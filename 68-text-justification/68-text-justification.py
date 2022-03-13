class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buf = []
        blen = 0
        r = []
        for i, w in enumerate(words):
            # sum of chars in words array
            blen = sum([len(b) for b in buf])
            if blen + len(buf) + len(w) > maxWidth:
                #flush
                spaces = maxWidth - blen
               
                splen = spaces if len(buf) == 1 else spaces//(len(buf)-1)
                extra = 0 if len(buf) == 1 else spaces%(len(buf)-1)
               
                spaces_str = "".ljust(splen, ' ')
                # use spaces_str+" " to join elements in buf array before extra+1
                snt = (spaces_str+" ").join(buf[:extra+1])+ spaces_str
                snt += spaces_str.join(buf[extra+1:])
               
                r.append(snt)
                del buf
                buf = []
           
            buf.append(w)
        snt = " ".join(buf)
        snt = snt.ljust(maxWidth, " ")
        r.append( snt )
        return r
        
#         n = 0
#         lst = []
#         res = []
        
#         for i,w in enumerate(words):
#             if n != 0:
#                 n += 1
                
#             if n + len(w) <= maxWidth:
#                 lst.append(w)
#                 n += len(w)
                
#             else:
#                 spaces = (maxWidth - n)//(len(lst)-1) + 1
#                 rem = (maxWidth - n)%(len(lst)-1)
                
#                 print(spaces, rem)
                
#                 for l in range(len(lst) - 1):    
#                     lst[l] += " "*spaces +(" " if l<rem else "")
                    
#                 res.append("".join(lst))
                
#                 n = 0
#                 lst = []
            
#                 lst.append(w)
                
#         return res