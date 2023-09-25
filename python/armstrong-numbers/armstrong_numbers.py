def is_armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number
