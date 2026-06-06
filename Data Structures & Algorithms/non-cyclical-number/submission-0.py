class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def recurisve(n) -> bool:
            print(n, n in visit)
            if n in visit:
                print("HERE SO WE ARE RETURNING FALSE")
                return False
                print("NOT POSSIBLE")
            if n == 1:
                return True
            visit.add(n)
            sum = 0
            while n != 0:
                temp = n % 10
                sum += temp ** 2
                n = n // 10
            return recurisve(sum)
        return recurisve(n)