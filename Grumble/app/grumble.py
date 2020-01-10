def accum(letters: str) -> str:
    string = []
    for n in range(len(letters)):
        string.append((n+1) * letters[n])

    new_string = []
    for i in string:
        new_string.append(i.capitalize())

    accum = '-'.join(new_string)

    return accum
