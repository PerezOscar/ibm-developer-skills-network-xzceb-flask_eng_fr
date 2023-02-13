"""
Test module
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_not_eq(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")
    def test_exception_english(self):
        with self.assertRaises(TypeError):
            english_to_french()

class TestFrenchToEnglish(unittest.TestCase):
    def test_french(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_not_eq(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
    def test_exception_french(self):
        with self.assertRaises(TypeError):
            french_to_english()

unittest.main()
