from unittest import TestCase
from random import randrange

DATA = None


class TestSolutions(TestCase):
    @classmethod
    def setUpClass(cls):
        """Connect and load data needed by tests"""
        global DATA
        with open("Countries/tests/fixtures/countries.txt", mode="r") as f:
            DATA = f.read().splitlines()

    @classmethod
    def tearDownClass(cls):
        """Clean our data out"""
        DATA = None

    def test_united(self):
        """Should return countres with 'United'"""
        pass

    def test_begin_end_vowel(self):
        """Should return countries that begin and end with a vowel"""
        pass

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
