"""Applies your custom cipher algorithm."""


def encrypt(message, key):
    """Returns the given message encrypted using your custom cipher."""
    return charp(message, key)


def decrypt(message, key):
    """Returns the given message encrypted using your custom cipher."""
    return charp(message, -key)


def charp(charo, key):
    new_charo = ""
    for char in charo:
        new_charo += cipher_applied(char, key)

    return new_charo


def cipher_applied(message, key):
    alphabet = "zyxwvutsrqponmlkjihgfedcba"
    numbers = "1234567890"

    if message.lower() in alphabet:

        # Find the character that's 'shift' characters over.
        new_index = alphabet.index(message.lower()) + key
        shifted_letter = alphabet[new_index % len(alphabet)]

        if message.isupper():
            shifted_letter.lower()
        else:
            shifted_letter.upper()
        return shifted_letter

    elif message in numbers:
        message = str(message)
        if key % 2 != 0:
            new_numdex = numbers.index(message.lower()) + key
            shifted_letter = numbers[new_numdex % len(numbers)]
        else:
            key += 1
            new_numdex = numbers.index(message.lower()) + key
            shifted_letter = numbers[new_numdex % len(numbers)]
        return shifted_letter