def reverse_ascending(numbers):
    result = []
    ascending_sequence = []

    for index, current_value in enumerate(numbers):
        if index - 1 < 0:
            continue

        if current_value > numbers[index - 1]:
            if ascending_sequence:
                ascending_sequence.append(current_value)
            else:
                ascending_sequence.extend([numbers[index - 1], current_value])
        else:
            if ascending_sequence:
                result.extend(ascending_sequence[::-1])
                ascending_sequence.clear()
            else:
                result.append(numbers[index - 1])

    if ascending_sequence:
        result.extend(ascending_sequence[::-1])
    if len(result) != len(numbers):
        result.append(numbers[-1])

    return result
