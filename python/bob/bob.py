def response(s):
    s = s.strip()  # Strip leading and trailing whitespace

    # Check if the input string is empty after stripping whitespace
    if not s:
        return "Fine. Be that way!"
    # Check if the string is in uppercase (yelling) and ends with a question mark
    elif s.isupper() and s.endswith('?'):
        return "Calm down, I know what I'm doing!"
    # Check if the string is in uppercase (yelling)
    elif s.isupper():
        return "Whoa, chill out!"
    # Check if the string ends with a question mark
    elif s.endswith('?'):
        return "Sure."
    # For all other inputs
    else:
        return "Whatever."