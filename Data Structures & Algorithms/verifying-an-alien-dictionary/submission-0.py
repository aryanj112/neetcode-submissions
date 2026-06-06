class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def isSmaller(w1,w2):
            for i in range(min(len(w1),len(w2))):
                if mapping[w1[i]] < mapping[w2[i]]:
                    return True
                if mapping[w1[i]] > mapping[w2[i]]:
                    return False
            return len(w1) <= len(w2)
        
        mapping = {}
        for i in range(len(order)):
            mapping[order[i]] = i
        
        for i in range(0,len(words)-1):
            if not isSmaller(words[i],words[i+1]):
                return False
        return True