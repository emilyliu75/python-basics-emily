def count_even_numbers(value_list: list[int]) -> int:
    return len(
        [number for number in value_list if number % 2 == 0]
    )
