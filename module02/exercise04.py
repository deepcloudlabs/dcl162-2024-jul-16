def fun(numbers: list[int]) -> list[bool]:
    print(f"fun({numbers}) is working...")
    result: list[bool] = []
    for number in numbers:
        if number % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result


def gun(numbers: list[int]) -> list[bool]:
    print(f"gun({numbers}) is working...")
    for number in numbers:
        if number % 2 == 0:
            print(f"gun: {number} is even")
            yield True
        else:
            print(f"gun: {number} is odd")
            yield False


for is_bool in gun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(f"is even: {is_bool}")
