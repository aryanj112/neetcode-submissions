class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        s = [] # [temp, index]
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                T, I = s.pop()
                output[I] = i - I
            s.append([t, i])            

        return output
