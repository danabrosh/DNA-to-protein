# Tests the dna_to_mrna function with different DNA sequences.
from dna_functions import dna_to_mrna

def test_dna_to_mrna():
    assert dna_to_mrna("ATG") == "AUG"
    assert dna_to_mrna("TAC") == "UAC"
    assert dna_to_mrna("CGT") == "CGU"
    assert dna_to_mrna("XXX") == "XXX"  # stays the same if unknown



#Tests the codon_translation function with different 3-letter DNA codons.
from dna_functions import codon_translation

def test_codon_translation():
    assert codon_translation("ATG") == ("AUG", "Methionine")
    assert codon_translation("TTC") == ("UUC", "Phenylalanine")
    assert codon_translation("AAA") == ("AAA", "Lysine")
    assert codon_translation("CCC") == ("CCC", "Proline")
    assert codon_translation("GAA") == ("GAA", "Glutamic acid")


# Test the find_motif_positions function
from dna_functions import find_motif_positions

def test_find_motif_positions():
    seq = "ATGCATGCGTATATATAGC"
    assert find_motif_positions(seq, "ATG") == [0, 4]
    assert find_motif_positions(seq, "TATA") == [9, 11, 13]
    assert find_motif_positions(seq, "AAA") == []  


#Test the introduce_mutations function
from dna_functions import introduce_mutations

def test_introduce_mutations():
    dna_seq = "ATGCGTAC"
    num_mutations = 2
    mutated_seq, mutations = introduce_mutations(dna_seq, num_mutations)

    # Make sure the mutated sequence is the same length as the original
    assert len(mutated_seq) == len(dna_seq)

    # Check that we got the right number of mutations
    assert len(mutations) == num_mutations

    # Make sure each mutation actually changed a base
    for pos, orig, new in mutations:
        assert dna_seq[pos] == orig
        assert mutated_seq[pos] == new
        assert orig != new

