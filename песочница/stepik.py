from string import ascii_uppercase as up, ascii_lowercase as low

class CaesarCipher:

    _chars = {i:el for i, el in zip(range(26), low)}
    _Chars = {i:el for i, el in zip(range(26), up)}

    def __init__(self, x):
        self.x = x

    def encode(self, word: str):
        res = ''
        for let in word:
            if let in low:
                res = ''.join((res, self._chars[(low.index(let) + self.x)%26]))
            elif let in up:
                res = ''.join((res, self._Chars[(up.index(let) + self.x)%26]))
            else:
                res = ''.join((res, let))
        return res

    def decode(self, word: str):
        res = ''
        for let in word:
            if let in low:
                res = ''.join((res, self._chars[(low.index(let) - self.x) % 26]))
            elif let in up:
                res = ''.join((res, self._Chars[(up.index(let) - self.x) % 26]))
            else:
                res = ''.join((res, let))
        return res



