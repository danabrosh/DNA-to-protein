#Tests the codon_translation function with different 3-letter DNA codons.
from dna_functions import codon_translation

def test_codon_translation():
    assert codon_translation("ATG") == ("UAC", "Tyrosine")
    assert codon_translation("AAA") == ("UUU", "Phenylalanine")
    assert codon_translation("TTT") == ("AAA", "Lysine")
    assert codon_translation("CCC") == ("GGG", "Glycine")
    assert codon_translation("GAA") == ("CUU", "Leucine")