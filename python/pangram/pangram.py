def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    for char in sentence.lower():
        if char in alphabet:
            alphabet.remove(char)
    return len(alphabet) == 0
