class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cows = 0, 0
        ds, dt = {}, {}
        for i in range(len(secret)):
            if i < len(guess) and secret[i] == guess[i]:
                bull += 1
        for i in secret:
            ds[i] = ds.get(i, 0) + 1
        for i in guess:
            dt[i] = dt.get(i, 0) + 1
        for k in ds:
            if k in dt:
                cows += min(ds[k], dt[k])
        cows -= bull
        return str(bull) + 'A' + str(cows) + 'B'
