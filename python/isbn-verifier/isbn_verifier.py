def is_valid(isbn):
     # Remove hyphens
    isbn = isbn.replace('-', '')

    # Check length
    if len(isbn) != 10:
        return False

    # Compute sum
    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)

    # Check the last character
    if isbn[9] == 'X':
        total += 10
    elif isbn[9].isdigit():
        total += int(isbn[9])
    else:
        return False

    # Check if valid
    return total % 11 == 0
