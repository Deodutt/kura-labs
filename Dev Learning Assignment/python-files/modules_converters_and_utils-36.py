# def lbs_to_kg(weight):
#     return weight * 0.45


# def kg_to_lbs(weight):
#     return weight / 0.45


def find_max(numbers):
    max2 = numbers[0]
    for number in numbers:
        if number > max2:
            max2 = number
    return max2