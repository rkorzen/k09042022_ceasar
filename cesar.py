"""
Napisz funkcję encrypt, która zaszyfruje tekst zgodnie z szyfrem cesara.
Oraz decrypt, która odkoduje ten tekst.
"""


def encrypt(text: str, shift: int) -> str:
    """Cipher text with ceasar cipher
    Example:

    >>> encrypt("CEASER CIPHER DEMO", 4)
    'GIEWIVrGMTLIVrHIQS'
    >>> encrypt("A", 1)
    'B'

    """
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text: str, shift: int) -> str:
    """Decipher text with ceasar cipher

    >>> decrypt("GIEWIVrGMTLIVrHIQS", 4)
    'CEASER CIPHER DEMO'
    >>> decrypt("B", 1)
    'B'
    """
    result = ""
    space = chr((ord(" ") + shift - 97) % 26 + 97)
    for char in text:
        if char == space:
            result += " "
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    assert encrypt("CEASER CIPHER DEMO", 4) == "GIEWIVrGMTLIVrHIQS"
    assert encrypt("A", 1) == "B"
    assert decrypt("GIEWIVrGMTLIVrHIQS", 4) == "CEASER CIPHER DEMO"
    assert decrypt("B", 1) == "A"
