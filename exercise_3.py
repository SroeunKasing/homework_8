def remove_all_after(numbers, n):
    
    result_list = []
    
    for number in numbers:
        if number == n:
            result_list.append(number)
            break
        result_list.append(number)
    return result_list
