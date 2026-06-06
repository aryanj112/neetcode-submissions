class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # given a list of triplets if any one triplet has a value
        # that is larger than the value at the target it is useless since 
        # using it would mean getting away from our target
        # so we want to go through the list and for every element just go through
        # and see if we need it and if it helps our output
        t0, t1, t2 = target[0], target[1], target[2]
        is_t0, is_t1, is_t2 = False, False, False

        for triplet in triplets:
            v0, v1, v2 = triplet[0], triplet[1], triplet[2]

            # first check if its a valid triplet:
            if v0 <= t0 and v1 <= t1 and v2 <= t2:
                # this is a valid triple
                if v0 == t0:
                    is_t0 = True
                if v1 == t1:
                    is_t1 = True
                if v2 == t2:
                    is_t2 = True

        return is_t0 and is_t1 and is_t2