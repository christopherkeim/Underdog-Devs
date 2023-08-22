from unittest import TestCase
from random import randrange
from Countries.solutions import get_united, get_begin_end_vowel


class TestSolutions(TestCase):
    @classmethod
    def setUpClass(cls):
        """Connect and load data needed by tests"""
        with open("./Countries/tests/fixtures/countries.txt", mode="r") as f:
            cls.DATA = f.read().splitlines()

    @classmethod
    def tearDownClass(cls):
        """Clean our data out"""
        pass

    def test_united(self):
        """Should return countres with 'United'"""
        united_words = get_united.get_united(self.DATA)
        r = randrange(0, len(united_words))
        self.assertEqual(len(united_words), 3)
        self.assertEqual(
            united_words,
            ["United Arab Emirates", "United Kingdom", "United States of America"],
        )
        self.assertTrue("United" in united_words[r])
        # Sad paths
        self.assertRaises(TypeError, get_united, [1, 2, 3, 4])

    def test_get_begin_end_vowel(self):
        """Should return countries that begin and end with a vowel"""
        vowel_countries = get_begin_end_vowel.get_begin_end_vowel(self.DATA)
        r = randrange(0, len(vowel_countries))
        self.assertTrue("United States of America" in vowel_countries)
        self.assertTrue("India" in vowel_countries)
        self.assertFalse("Somalia" in vowel_countries)
        self.assertFalse("Italy" in vowel_countries)
        # Sad paths
        self.assertRaises(TypeError, get_begin_end_vowel, [1, 2, 3, 4])
        self.assertRaises(TypeError, get_begin_end_vowel, "Hello")

    def test_gt_50_percent_vowel(self):
        """Should return countries that are > 50% vowels"""
        pass

    def test_shortest_country_name(self):
        """Should return the country with shortest name handling ties"""
        pass

    def test_only_one_vowel(self):
        """Should return countries containing only one vowel handling multiple instances of vowel"""
        pass

    def test_country_name_inside_other(self):
        """Should return a countries with names contained inside other country names"""
        pass
