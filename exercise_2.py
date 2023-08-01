def index_power(numbers, n):
    return numbers[n] ** n if -len(numbers) <= n < len(numbers) else -1
