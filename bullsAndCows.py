class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        m ={}
        bulls = 0
        c = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
            else:
                if m.get(secret[i]):
                    m[secret[i]] +=1
                else:
                    m[secret[i]] = 1
        seen = {}
        for i in range(len(guess)):
            if m.get(guess[i]) > 0 and secret[i] != guess[i]:
                c += 1
                m[guess[i]] -= 1

        return str(bulls)+'A'+str(c)+'B'