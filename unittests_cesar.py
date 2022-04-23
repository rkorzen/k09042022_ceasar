import unittest
from cesar import encrypt, decrypt


class TestEncryptFunction(unittest.TestCase):
    def test_simple_encrypt_big_letter(self):
        self.assertEqual(encrypt("A", 1), "B")

    def test_simple_encrypt_small_letter(self):
        self.assertEqual(encrypt("a", 2), "c")

    def test_simple_sentece_big_letter(self):
        self.assertEqual(encrypt("CEASER CIPHER DEMO", 4), "GIEWIVrGMTLIVrHIQS")

    def test_simple_sentece_small_letter(self):
        self.assertEqual(encrypt("ceaser cipher demo", 4), "giewivrgmtlivrhiqs")

    def test_space(self):
        self.assertEqual(encrypt("n ", 4), "rr")


class TestDecryptFunction(unittest.TestCase):
    def test_simple_encrypt_big_letter(self):
        self.assertEqual(decrypt("B", 1), "A")

    def test_simple_encrypt_small_letter(self):
        self.assertEqual(decrypt("c", 2), "a")

    def test_simple_sentece_big_letter(self):
        self.assertEqual(decrypt("GIEWIVrGMTLIVrHIQS", 4), "CEASER CIPHER DEMO")

    def test_simple_sentece_small_letter(self):
        self.assertEqual(decrypt("giewivrgmtlivrhiqs", 4), "ceaser cipher demo")

    def test_space(self):
        self.assertEqual(decrypt("rr", 4), "  ")
