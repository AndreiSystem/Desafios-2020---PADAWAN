class Kata:
    def __init__(self):
        self._middle = ''


    def get_middle(self, string: str) -> str:
        if len(string) % 2 == 0:
            index = int(len(string) / 2)
            self._middle = string[index - 1] + string[index]
        else:
            index = int(len(string) / 2)
            self._middle = string[index]

        return self._middle
