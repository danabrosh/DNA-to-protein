import random #imoort needed for mutation simulation
#rna to amino acid translation dictionary
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

#Codon translation function
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
            mRNA_codon += 'N'  # Invalid base

    print(f"\nmRNA codon: {mRNA_codon}")
    
    # Amino acid translation
    amino_acid = codon_table.get(mRNA_codon, "Unknown")
    print(f"{mRNA_codon} → {amino_acid}")
    return mRNA_codon, amino_acid

#Reading frames function
def reading_frames():
    dna_seq = get_dna_sequence()  # Get the DNA sequence from the user

    # Check if the sequence is valid
    if dna_seq is None or dna_seq == "":
        print("No DNA sequence provided.")
        return
    if len(dna_seq) < 3:
        print("Please enter a DNA sequence with at least 3 nucleotides.")
        return

    # Dictionaries for conversion
    dna_complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna_to_mrna_bases = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Forward and reverse strands
    strands = {
        "Forward": dna_seq,
        "Reverse": "".join(dna_complement.get(base, 'N') for base in reversed(dna_seq))
    }

    # For each strand
    for strand_name, strand_seq in strands.items():
        # Convert DNA to mRNA
        mrna_seq = "".join(dna_to_mrna_bases.get(base, 'N') for base in strand_seq)

        print(f"\n{strand_name} strand reading frames:")

        # For each of the 3 reading frames
        for frame in range(3):
            print(f"\nFrame {frame + 1}:")
            i = frame
            found_orf = False
            in_orf = False
            while i + 3 <= len(mrna_seq):
                codon = mrna_seq[i:i+3]
                amino_acid = codon_table.get(codon, 'X')

                if codon == 'AUG':
                    in_orf = True
                    print(f"{codon} → {amino_acid}")
                elif in_orf:
                    print(f"{codon} → {amino_acid}")
                    if amino_acid == 'STOP':
                        found_orf = True
                        break
                i += 3

            if not found_orf:
                print("No open reading frame")


# Motif search function
def motif_search():
    dna_seq = get_dna_sequence()  # Get the DNA sequence from the user

    if dna_seq is None or dna_seq == "":
        print("No DNA sequence provided.")
        return

    print("\nMotif Search:")  # The user can search for a known motif or enter a custom one
    print("1. Search for a known motif (e.g., TATA, CG)")
    print("2. Enter your own custom motif")
    choice = input("Enter 1 or 2: ").strip()

    motif_lst = {
        "1": ("TATA", "Promoter box"),
        "2": ("CG", "CpG site"),
        "3": ("AATAAA", "Polyadenylation signal"),
        "4": ("CAG", "Repeat motif"),
        "5": ("TTAGGG", "Telomere repeat")}

    if choice == '1':  # Choose from the motif list
        print("\nSelect one of the following motifs to search for:")
        for num, (motif, description) in motif_lst.items():
            print(f"{num}. {motif} ({description})")
        selected = input("Enter the number of the motif you want to search for: ").strip()
        if selected in motif_lst:
            motif = motif_lst[selected][0]
        else:
            print("Invalid selection.")
            return
    elif choice == '2':  # Custom motif
        motif = input("Enter the motif you want to search for: ").strip().upper()
        if motif == "":
            print("No motif entered.")
            return
    else:
        print("Invalid choice.")
        return

    # Search and display results from the DNA sequence
    count = dna_seq.count(motif)
    positions = [i for i in range(len(dna_seq)) if dna_seq.startswith(motif, i)]
    print(f"\nMotif '{motif}':")
    print(f"Found {count} time(s) at positions: {positions if positions else 'None'}")

# Mutation simulation function 
def mutation_simulation():
    dna_seq = get_dna_sequence()  # Get DNA from user
    if dna_seq is None or dna_seq == "":
        print("No DNA sequence provided.")
        return
    try:
        num_mutations = int(input("Enter the number of mutations to introduce: "))
    except ValueError:
        print("Invalid number entered.")
        return

    if num_mutations < 1 or num_mutations > len(dna_seq):
        print("Invalid number of mutations.")
        return
    dna_bases = ['A', 'T', 'C', 'G']
    dna_list = list(dna_seq)  # Convert DNA sequence to a list for mutations
    mutations = []  # mutations list
    positions = random.sample(range(len(dna_seq)), num_mutations)
    for pos in positions:
        original_base = dna_list[pos]
        new_base = random.choice([b for b in dna_bases if b != original_base])
        dna_list[pos] = new_base
        mutations.append((pos, original_base, new_base))
        mutated_seq = ''.join(dna_list)

        print("\nOriginal DNA sequence:")
        print(dna_seq)
        print("\nMutated DNA sequence:")
        print(mutated_seq)

    print("\nMutations introduced:")
    for pos, orig, new in mutations:
        print(f"Position {pos + 1}: {orig} → {new}")

