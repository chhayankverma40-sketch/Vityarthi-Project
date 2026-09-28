import unittest
from modules.sequence import *
from modules.analysis import *
class TestDNA(unittest.TestCase):
    def test_all(self):
        self.assertTrue(validate_sequence("ACGT"))
        self.assertEqual(nucleotide_count("AAGCTT"),{"A":2,"C":1,"G":1,"T":2})
        self.assertEqual(complement_sequence("ACGT"),"TGCA")
        self.assertEqual(transcribe_dna("ACGT"),"UGCA")
        self.assertEqual(find_motif("AATCGATCG","TCG"),[3,7])
        self.assertEqual(compare_sequences("ACGT","ACGA")["matches"],3)
if __name__=="__main__": unittest.main()
