from unittest import TestCase
from More_Wordplay.solutions.get_all_rstlne import get_all_rstlne


class TestSolutions(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """Connect and load data needed by tests"""
        # Scrabble Words
        with open("./More_Wordplay/tests/fixtures/sowpods.txt", mode="r") as f:
            cls.SCRABBLE = f.read().split()

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean our data out"""
        cls.SCRABBLE = None

    def test_get_all_rstlne(self):
        """It should return all words made from only 'RSTLNE'"""
        rstlne_words: list[str] = get_all_rstlne(self.SCRABBLE)
        self.assertTrue("TREE" in rstlne_words)
        self.assertTrue("LENSLESS" in rstlne_words)
        self.assertTrue("ENTREE" in rstlne_words)
        self.assertFalse("AARDVARK" in rstlne_words)
        self.assertFalse("PANDORE" in rstlne_words)
        self.assertFalse("SECONDARY" in rstlne_words)
        # Sad paths
