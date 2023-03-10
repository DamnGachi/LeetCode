class Solution:
    def canMakeArithmeticProgression(self, l: List[int]) -> bool:
        l = sorted(l)
        delta = l[1] - l[0]
        for index in range(len(l) - 1):
            if not (l[index + 1] - l[index] == delta):
                return False
        return True
