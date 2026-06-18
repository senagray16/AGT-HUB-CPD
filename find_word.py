class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        b = 0
        for i in words:
            a = 0
            c = list(chars[:])
            for j in i:
                if j not in c:
                    a = 1
                    break
                else:
                    c.remove(j)
            if a == 0:
                b +=len(i)
        
        return b
                
        
