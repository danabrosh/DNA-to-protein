#rna to amino acid translation
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

# Function to get DNA sequence from user
def get_dna_sequence():
    print("How would you like to provide the DNA sequence?")
    print("1. Enter sequence manually")
    print("2. Load from FASTA file")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        seq = input("Enter the DNA sequence: ").strip().upper()
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

#codon translation function
def codon_translation(dna_seq):  # Added parameter
    if dna_seq is None or dna_seq == "":
        print("No DNA sequence provided.")
        return

    if len(dna_seq) != 3:
        print("Please enter exactly 3 nucleotides.")
        return

    mRNA_codon = ""
    for base in dna_seq:
        if base == 'A':
            mRNA_codon += 'U'
        elif base == 'T':
            mRNA_codon += 'A'
        elif base == 'C':
            mRNA_codon += 'G'
        elif base == 'G':
            mRNA_codon += 'C'
        else:
            mRNA_codon += 'N'  # invalid base

    print(f"\nmRNA codon: {mRNA_codon}")

    # amino acid translation
    amino_acid = codon_table.get(mRNA_codon, "Unknown")
    print(f"{mRNA_codon} → {amino_acid}")

def reading_frames():
    pass  # You'll implement this function later

def motif_search():
    pass  # You'll implement this function later

def mutation_simulation():
    pass  # You'll implement this function later