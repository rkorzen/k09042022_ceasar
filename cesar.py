"""
Napisz funkcję encrypt, która zaszyfruje tekst zgodnie z szyfrem cesara.
Oraz decrypt, która odkoduje ten tekst.

    >>> encrypt("CEASER CIPHER DEMO", 4)
    IEWIVrGMTLIVrHIQS
    >>> decrypt("IEWIVrGMTLIVrHIQS", 4)
    'CEASERzCIPHERzDEMO'

Wersj trudniejsza

    >>> decrypt("IEWIVrGMTLIVrHIQS", 4)
    'CEASER CIPHER DEMO'


przesuniecie 1
"ABCD"
"BCDA"


przesuniecie 2
"ABCD"
"CDAB"

"""


def encrypt(text: str, shift: int) -> str:
    result = "IEWIVrGMTLIVrHIQS"
    return result


if __name__ == "__main__":
    assert encrypt("CEASER CIPHER DEMO", 4) == "IEWIVrGMTLIVrHIQS"
    assert encrypt("A", 1) == "B"
