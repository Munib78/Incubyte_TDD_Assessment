def add(input_string) -> int:

    """This is the second case where it should  handle any amount of numbers."""

    nums = input_string.split(",")

    sums_nums = 0

    for j in nums:
        sums_nums = sums_nums + int(j)

    return sums_nums
