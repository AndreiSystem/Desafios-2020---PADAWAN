
class DoubleSort:
    def __init__(self, list_user:list):
        self._list_user = list_user

    def return_list_sort(self) -> list:
        list_string = []
        list_numbers = []

        for item in self._list_user:
            if isinstance(item, str):
                list_string.append(item)
            else:
                list_numbers.append(item)


        list_string.sort()
        list_numbers.sort()
        return list_numbers + list_string