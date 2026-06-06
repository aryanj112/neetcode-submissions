class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = defaultdict(int)
        for n in hand:
            count[n] += 1

        for _ in range(len(hand) // groupSize):
            keys = sorted(count.keys())
            minimum = keys[0]
            count[minimum] -= 1
            if count[minimum] == 0:
                count.pop(minimum) 

            for j in range(1, groupSize, 1):
                if count[minimum + j] > 0:
                    count[minimum + j] -= 1
                    if count[minimum + j] == 0:
                        count.pop(minimum + j)
                else:
                    return False
        return True