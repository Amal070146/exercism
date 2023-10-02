def is_isogram(phrase):
    letters_seen = set()
    for char in phrase.lower():
        if char.isalpha():  # Check if the character is a letter
            if char in letters_seen:
                return False
            letters_seen.add(char)
    return True