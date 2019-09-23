# noinspection PyUnusedLocal
def fizz_buzz(number):
    number_str = str(number)
    result = ""
    if number_str.find("3") >= 0 or number % 3 == 0:
        result = "fizz"
    if number_str.find("5") >= 0 or number % 5 == 0:
        if not result.strip():
            result = "buzz"
        else:
            result = "fizz buzz"
    return result
