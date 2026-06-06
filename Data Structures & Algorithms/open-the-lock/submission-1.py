class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        q = deque()
        visit = set()
        q.append("0000")
        visit.add("0000")        

        def children(combo):
            res = []
            for w in range(4):
                decrement = int(combo[w]) - 1
                increment = int(combo[w]) + 1
                if decrement < 0: decrement = 9
                if increment > 9: increment = 0
                res.append(combo[:w] + str(decrement) + combo[w+1:])
                res.append(combo[:w] + str(increment) + combo[w+1:])
            return res

        turns = 0
        while q:
            for _ in range(len(q)):
                combo = q.popleft()
                if combo in deadends_set:
                    return -1
                if combo == target:
                    return turns
                for child in children(combo):
                    if child in visit or child in deadends_set:
                        continue
                    q.append(child)
                    visit.add(child)
            turns += 1

        return -1