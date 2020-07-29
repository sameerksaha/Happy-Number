class Solution:
    def isHappy(self, n: int) -> bool:
        table = {}
        while n > 0:
            s = sum([pow(int(i), 2) for i in str(n)])
            if s not in table:
                table[s] = 1
            else:
                table[s] = table[s] + 1
                return False
            if s == 1:
                return True
            n = s
