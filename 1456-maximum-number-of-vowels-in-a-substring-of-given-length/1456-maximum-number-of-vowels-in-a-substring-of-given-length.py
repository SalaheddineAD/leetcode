class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s = [1 if i in {'a', 'e', 'i', 'o', 'u'} else 0 for i in s]
        win = sum(s[:k])
        max_win = win
        
        for i in range(k, len(s)):
            if s[i]:
                win += 1
            if s[i-k]:
                win -= 1
            if max_win < win:
                max_win = win
            if win >= k:
                return k
        return max_win
            