def reverse_ascending(numbers):
    result = []
    ascending_sequence = []

    for index, current_value in enumerate(numbers):
        # we don't want to compare between the first and the last
        if index - 1 < 0:
            continue

        # main operation check for ascending
        if current_value > numbers[index - 1]:
            if ascending_sequence:
                # ascending has happened before
                ascending_sequence.append(current_value)
            else:
                # start noticing ascending
                ascending_sequence.extend([numbers[index - 1], current_value])

        # ascending has stopped
        else:
            # when noticing ascending has stopped
            if ascending_sequence:
                result.extend(ascending_sequence[::-1])
                ascending_sequence.clear()
            # ascending still has not started
            else:
                result.append(numbers[index - 1])

    # if ascending has never stopped
    if ascending_sequence:
        result.extend(ascending_sequence[::-1])

    # if ascending has never started
    if len(result) != len(numbers):
        result.append(numbers[-1])

    return result
