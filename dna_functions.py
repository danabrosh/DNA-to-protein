#Import needed for mutation simulation
import random 

#RNA to amino acid translation dictionary
codon_table = {
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
    'AUG': 'Methionine',
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UAA': 'STOP', 'UAG': 'STOP',
    'CAU': 'Histidine', 'CAC': 'Histidine',
    'CAA': 'Glutamine', 'CAG': 'Glutamine',
    'AAU': 'Asparagine', 'AAC': 'Asparagine',
    'AAA': 'Lysine', 'AAG': 'Lysine',
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGA': 'STOP',
    'UGG': 'Tryptophan',
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
    'AGU': 'Serine', 'AGC': 'Serine',
    'AGA': 'Arginine', 'AGG': 'Arginine',
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'
}

# Function to transcribe DNA to mRNA- stimulates transcription
def dna_to_mrna(dna_seq):
    rna_complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    mrna = ''.join(rna_complement.get(base, 'N') for base in reversed(dna_seq))
    return mrna

# Function to get DNA sequence from user
def get_dna_sequence():
    print("How would you like to provide the DNA sequence?")
    print("1. Enter sequence manually")
    print("2. Load from FASTA file")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        seq = input("Enter the DNA sequence: ").strip().upper()
        #Only allow valid DNA bases- error if invalid bases
        if not all(base in "ATCG" for base in seq):
            print("Invalid DNA sequence. Use only A, T, C, G.")
            return None
        return seq

    elif choice == '2':
        file_path = input("Enter the path to the FASTA file: ").strip()
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                seq = ""
                for line in lines:
                    if not line.startswith('>'):
                        seq += line.strip().upper()
                return seq
        except FileNotFoundError:
            print("Error: file not found.")
            return None

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return None


#DNA codon translation function
#Translate a DNA codon to mRNA and amino acid
def codon_translation(dna_seq):  
    if len(dna_seq) != 3:
        print("Please enter exactly 3 nucleotides.")
        return

    # Transcribe from template strand to mRNA codon
    mRNA_codon = dna_to_mrna(dna_seq)
    print(f"\nmRNA codon: {mRNA_codon}")

    amino_acid = codon_table.get(mRNA_codon, "Unknown")
    print(f"{mRNA_codon} → {amino_acid}")

    return mRNA_codon, amino_acid


# Reading frames function: Finds ORFs in mRNA transcribed from DNA template strand
def reading_frames():
    dna_seq = get_dna_sequence()

    if not dna_seq or len(dna_seq) < 3:
        print("No valid DNA sequence provided.")
        return

    mrna_seq = dna_to_mrna(dna_seq)  # Transcribe from template to mRNA
    print("\nmRNA sequence (5'→3'):", mrna_seq)

    for frame in range(3):
        print(f"\nFrame {frame + 1}:")
        i = frame
        orf_codons = []
        found_orf = False

        while i + 3 <= len(mrna_seq):
            codon = mrna_seq[i:i+3]
            amino_acid = codon_table.get(codon, 'X')

            if codon == 'AUG' and not orf_codons:
                orf_codons.append((codon, amino_acid))
            elif orf_codons:
                orf_codons.append((codon, amino_acid))
                if amino_acid == 'STOP':
                    found_orf = True
                    break
            i += 3

        if found_orf:
            print("→ ORF found:")
            for codon, aa in orf_codons:
                print(f"{codon} → {aa}")
        else:
            print("No valid ORF (start+stop codons) found in this frame.")


#Functions for motif search
#Motןf search function finds motifs in the DNA sequence
def find_motif_positions(dna_seq, motif):
    return [i for i in range(len(dna_seq)) if dna_seq.startswith(motif, i)]

def motif_search():
    dna_seq = get_dna_sequence()
    if not dna_seq:
        print("No DNA sequence provided.")
        return

    print("\nMotif Search:")
    print("1. Choose from known motifs\n2. Enter custom motif")
    choice = input("Enter 1 or 2: ").strip()

    motif_lst = {
        "1": ("TATA", "Promoter box"),
        "2": ("CG", "CpG site"),
        "3": ("AATAAA", "Polyadenylation signal"),
        "4": ("CAG", "Repeat motif"),
        "5": ("TTAGGG", "Telomere repeat")
    }

    if choice == '1':
        for num, (motif, desc) in motif_lst.items():
            print(f"{num}. {motif} ({desc})")
        selected = motif_lst.get(input("Enter motif number: ").strip())
        if not selected:
            print("Invalid selection.")
            return
        motif = selected[0]
    elif choice == '2':
        motif = input("Enter custom motif: ").strip().upper()
        if not motif:
            print("No motif entered.")
            return
    else:
        print("Invalid choice.")
        return

    positions = find_motif_positions(dna_seq, motif)
    print(f"\nMotif '{motif}': Found {len(positions)} time(s) at positions: {positions or 'None'}")

# Mutation simulation function 
# This function introduces random mutations into a DNA sequence
def introduce_mutations(dna_seq, num_mutations): 
    dna_bases = ['A', 'T', 'C', 'G']
    dna_list = list(dna_seq)
    mutations = []
    positions = random.sample(range(len(dna_seq)), num_mutations)

    for pos in positions:
        original_base = dna_list[pos]
        new_base = random.choice([b for b in dna_bases if b != original_base])
        dna_list[pos] = new_base
        mutations.append((pos, original_base, new_base))

    mutated_seq = ''.join(dna_list)
    return mutated_seq, mutations

# Mutation simulation function - this function simulates mutations in a DNA sequence
def mutation_simulation():
    dna_seq = get_dna_sequence()
    if not dna_seq:
        print("No DNA sequence provided.")
        return

    try:
        num_mutations = int(input("Enter number of mutations: "))
    except ValueError:
        print("Invalid number.")
        return

    if not (1 <= num_mutations <= len(dna_seq)):
        print("Invalid number of mutations.")
        return

    mutated_seq, mutations = introduce_mutations(dna_seq, num_mutations)

    print(f"\nOriginal DNA sequence:\n{dna_seq}")
    print(f"\nMutated DNA sequence:\n{mutated_seq}")
    print("\nMutations introduced:")
    for pos, orig, new in mutations:
        print(f"Position {pos + 1}: {orig} → {new}")
