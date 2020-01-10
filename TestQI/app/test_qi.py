def iq_test(numbers: str) -> int:
    list_numbers = numbers.split()

    int_numbers = [int(numbers) for numbers in list_numbers]

    list_odd = []
    list_even = []

    for numbers in int_numbers:
        if numbers % 2 == 0:
            list_even.append(numbers)
        else:
            list_odd.append(numbers)

    return int_numbers.index(list_even[0]) + 1 if len(list_odd) > len(list_even) else int_numbers.index(list_odd[0]) + 1






