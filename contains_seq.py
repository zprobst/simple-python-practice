import unittest


def contains_sequence(dna_sequence, subsequence):
    """
    Checks if a defined subsequence exists in a sequence of dna.

    :param dna_sequence: The dna sequence to check in for a subsequence.
        ex: ['a', 't', 'g', ...]
    
    :param subsequence: The subsequence of the dna to check for.
    :return: True if the subsequence exists in python.
    """
    pass


class TestContainsSequence(unittest.TestCase):
    sequence = list(
        "atgtggacactacagaatggcggagagagaattgctaaagccagttcagccggctcagag"
    )
    
    def test_small_sequence(self):
        sub = list("tggcggag")
        self.assertTrue(self.sequence, sub)
        
    def test_large_sequence(self):
        sub = list("ggcggagagagaat")
        self.assertTrue(self.sequence, sub)
        
    def test_no_sequence(self):
        sub = list("ttttttaaaaaaaagggggggggg")
        self.assertTrue(self.sequence, sub)


if __name__ == '__main__':
    unittest.main()
