# noinspection PyUnusedLocal
def check_deluxe(number_str):
    length = len(number_str)
    for i in range(1, length):
        if number_str[i] != number_str[0]:
            return False

    return True

def is_fake_deluxe(number):
    if number%2!=0:
        return "True"
    return "False"
def fizz_buzz(number):
    number_str = str(number)
    result = ""
    if number_str.find("3") >= 0 or number % 3 == 0:
        result = "fizz"
    if number_str.find("5") >= 0 or number % 5 == 0:
        if not result.strip():
            result = "buzz"
        else :
            result = "fizz buzz"
    if number >= 10 and check_deluxe(number_str):
        if is_fake_deluxe(number) == "True":
            result = result + " fake deluxe"
        elif is_fake_deluxe(number) == "False":
            result = result + " deluxe"
    if not result.strip():
        result = number

    return result

