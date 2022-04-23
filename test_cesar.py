import pytest
from cesar import encrypt, decrypt


@pytest.mark.parametrize(
    "text,shift,result",
    [
        ("A", 1, "B"),
        ("a", 2, "c"),
        ("CEASER CIPHER DEMO", 4, "GIEWIVrGMTLIVrHIQS"),
        ("ceaser cipher demo", 4, "giewivrgmtlivrhiqs"),
        ("n ", 4, "rr"),
    ],
)
def test_encrypt(text, shift, result):
    assert encrypt(text, shift) == result


# class TestEncryptFunction:
#     def test_simple_encrypt_big_letter(self):
#         assert encrypt("A", 1) == "B"
#
#     def test_simple_encrypt_small_letter(self):
#         assert encrypt("a", 2) == "c"
#
#     def test_simple_sentece_big_letter(self):
#         assert encrypt("CEASER CIPHER DEMO", 4) == "GIEWIVrGMTLIVrHIQS"
#
#     def test_simple_sentece_small_letter(self):
#         assert encrypt("ceaser cipher demo", 4) == "giewivrgmtlivrhiqs"
#
#     def test_space(self):
#         assert encrypt("n ", 4) == "rr"
#


class TestDecryptFunction:
    def test_simple_encrypt_big_letter(self):
        assert decrypt("B", 1) == "A"

    def test_simple_encrypt_small_letter(self):
        assert decrypt("c", 2) == "a"

    def test_simple_sentece_big_letter(self):
        assert decrypt("GIEWIVrGMTLIVrHIQS", 4) == "CEASER CIPHER DEMO"

    def test_simple_sentece_small_letter(self):
        assert decrypt("giewivrgmtlivrhiqs", 4) == "ceaser cipher demo"

    def test_space(self):
        assert decrypt("rr", 4) == "  "
