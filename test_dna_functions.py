# Tests the dna_to_mrna function with DNA template strand input
from dna_functions import dna_to_mrna

def test_dna_to_mrna():
    assert dna_to_mrna("ATG") == "CAU"
    assert dna_to_mrna("TAC") == "GUA"
    assert dna_to_mrna("CGT") == "ACG"
    assert dna_to_mrna("XXX") == "NNN"  # 'X' not recognized, becomes 'N'


# Tests the codon_translation function using DNA template strand
from dna_functions import codon_translation

def test_codon_translation():
    assert codon_translation("CAT") == ("AUG", "Methionine")
    assert codon_translation("GAA") == ("UUC", "Phenylalanine")
    assert codon_translation("TTT") == ("AAA", "Lysine")
    assert codon_translation("GGG") == ("CCC", "Proline")
    assert codon_translation("CTT") == ("AAG", "Lysine")

# Test the find_motif_positions function
from dna_functions import find_motif_positions

def test_find_motif_positions():
    seq = "ATGCATGCGTATATATAGC"
    assert find_motif_positions(seq, "ATG") == [0, 4]
    assert find_motif_positions(seq, "TATA") == [9, 11, 13]
    assert find_motif_positions(seq, "AAA") == []  


# Test the introduce_mutations function
from dna_functions import introduce_mutations

def test_introduce_mutations():
    dna_seq = "ATGCGTAC"
    num_mutations = 2
    mutated_seq, mutations = introduce_mutations(dna_seq, num_mutations)

    # Ensure the mutated sequence is the same length as the original
    assert len(mutated_seq) == len(dna_seq)

    # Check the number of mutations
    assert len(mutations) == num_mutations

    # Ensure each mutation changed a base
    for pos, orig, new in mutations:
        assert dna_seq[pos] == orig
        assert mutated_seq[pos] == new
        assert orig != new
