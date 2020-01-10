class ShorterWord:
    def __init__(self, phrase: str):
        self._phrase = phrase.split()

    def find_short(self) -> int:
        smallest_word = []

        for word in self._phrase:
            word = self.clear_word_simbols(word)
            smallest_word.append(len(word))
        try:
            return min(smallest_word)
        except:
            return 0

    def clear_word_simbols(self, word: str) -> str:
        clear_word = ''

        for letter in word:
            if letter.isalpha():
                clear_word += letter

        return clear_word







