class VowelCount:
    def __init__(self):
        self._vowel = ['a', 'e', 'i', 'o', 'u']


    def check_word(self, string: str) -> int:
        _count = 0

        for letters in string.lower():
            if letters in self._vowel:
                _count += 1
        return _count


