# Tests the dna_to_mrna function with different DNA sequences.
from dna_functions import dna_to_mrna

def test_dna_to_mrna():
    assert dna_to_mrna("ATG") == "UAC"
    assert dna_to_mrna("TAC") == "AUG"
    assert dna_to_mrna("CGT") == "GCA"
    assert dna_to_mrna("XXX") == "NNN"  # Invalid bases


#Tests the codon_translation function with different 3-letter DNA codons.
from dna_functions import codon_translation

def test_codon_translation():
    assert codon_translation("ATG") == ("UAC", "Tyrosine")
    assert codon_translation("AAA") == ("UUU", "Phenylalanine")
    assert codon_translation("TTT") == ("AAA", "Lysine")
    assert codon_translation("CCC") == ("GGG", "Glycine")
    assert codon_translation("GAA") == ("CUU", "Leucine")