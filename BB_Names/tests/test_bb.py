from unittest import TestCase
from BB_Names.solutions.get_shortest_in_top_40 import get_shortest_in_top_40
from BB_Names.solutions.get_longest_in_top_40 import get_longest_in_top_40


class TestSolutions(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """Connect and load data needed by tests"""
        # baby names 2020
        with open(
            "./BB_Names/tests/fixtures/baby_names_2020_short.txt", mode="r"
        ) as f1:
            cls.BABY2020 = f1.read().split()

        # baby names 1880
        with open(
            "./BB_Names/tests/fixtures/baby_names_1880_short.txt", mode="r"
        ) as f2:
            cls.BABY1880 = f2.read().split()

        # scrabble words
        with open("./BB_Names/tests/fixtures/sowpods.txt", mode="r") as f3:
            cls.SCRABBLE = f3.read().split()

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean our data out"""
        cls.BABY2020 = None
        cls.BABY1880 = None
        cls.SCRABBLE = None

    def test_get_shortest_in_top_40(self):
        """
        Should return the shortest name in the top 40 baby names
        for 2020.
        """
        shortest_name = get_shortest_in_top_40(self.BABY2020)
        self.assertEqual(len(shortest_name), 3)
        self.assertEqual(shortest_name, "Leo")
        self.assertNotEqual(shortest_name, "Liam")
        # Sad paths
        self.assertRaises(TypeError, get_shortest_in_top_40, [1, 2, 3, 4])
        self.assertRaises(TypeError, get_shortest_in_top_40, "Hello")

    def test_get_longest_in_top_40(self):
        """
        Should return the longest name in the top 40 baby names
        for 2020, handling ties.
        """
        longest_names = get_longest_in_top_40(self.BABY2020)
        self.assertTrue("Sebastian" in longest_names)
        self.assertTrue("Alexander" in longest_names)
        self.assertEqual(len(longest_names), 2)
        self.assertFalse("Theodore" in longest_names)
        # Sad paths
        self.assertRaises(TypeError, get_longest_in_top_40, [1, 2, 3, 4])
        self.assertRaises(TypeError, get_longest_in_top_40, "Hello")
        self.assertRaises(ValueError, get_longest_in_top_40, [""])

    def test_get_backwards_valid_scrabble(self):
        """
        Should return baby names that when spelled backwards are valid
        scrabble words.
        """

    def test_top_40_in_both_years(self):
        """
        Should return all of the names that were top 40 baby names in both
        2020 and 1880.
        """
        pass
