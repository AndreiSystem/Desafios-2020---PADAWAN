
def desc_order(numbers:int):
    list_numbers = [number for number in str(numbers)]

    list_numbers.sort(reverse=True)

    string = ''

    for n in list_numbers:
        string+=n


    return int(string)

