# noinspection PyUnusedLocal
def fizz_buzz(number):
    number=""+number

    if number%3==0 and number.find("3")>0:
        return "fizz"

    else:
        return number