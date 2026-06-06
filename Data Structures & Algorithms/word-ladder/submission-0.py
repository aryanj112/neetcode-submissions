class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        next_words = {wordList[i]:[] for i in range(len(wordList))}
        next_words[beginWord] = []
        
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        def oneApart(w1, w2):
            if len(w1) != len(w2):
                return False
        
            diff = 0
            i = 0
            while i < len(w1):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
                i += 1
            return diff == 1

        for w in wordList:
            if oneApart(beginWord,w):
                next_words[beginWord].append(w)
        
        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
                if oneApart(w1,w2):
                    next_words[w1].append(w2) 
                    next_words[w2].append(w1)
        print(next_words)
        
        visit = set()
        q = collections.deque()
        q.append((beginWord,1))
        visit.add(beginWord)
        while q: 
            for _ in range(len(q)):
                curr_word, count = q.popleft()
                if curr_word == endWord:
                    return count
                for next_word in next_words[curr_word]:
                    if next_word not in visit:
                        q.append((next_word, count + 1))
                        visit.add(next_word)
        return 0

        # curr_q : {cat,bat,sat,sag,bag}
        # q : {(sag,2),(dag,3),(sag,3)}
        # curr = sag
        # count = 2

        # cat : [bat, sat]
        # bat : [bag, sat]
        # bag : [bat, dag, sag]
        # sat : [bat,sag]
        # dag : [bag,sag]
        # dot : []