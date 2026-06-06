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
                        
            if count[minimum] == 1:
                count.pop(minimum)
            else:
                count[minimum] -= 1

            for i in range(1, groupSize, 1):
                next_num = minimum + i
                if count[next_num] == 1:
                    count.pop(next_num)
                elif count[next_num] > 1:
                    count[next_num] -= 1
                else:
                    return False
        return True