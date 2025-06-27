import random #Import needed for mutation simulation

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

# Function to transcribe DNA to mRNA
def dna_to_mrna(dna_seq):
    # This function takes a DNA coding strand (5'→3')
    # and returns the mRNA sequence by replacing T with U
    # (simulates transcription)
    return dna_seq.replace('T', 'U')


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
def codon_translation(dna_seq):  
    if dna_seq is None or dna_seq == "":
        print("No DNA sequence provided.")
        return

    if len(dna_seq) != 3:
        print("Please enter exactly 3 nucleotides.")
        return

    # Convert coding DNA to mRNA directly
    mRNA_codon = dna_seq.replace('T', 'U')
    print(f"\nmRNA codon: {mRNA_codon}")

    amino_acid = codon_table.get(mRNA_codon, "Unknown")
    print(f"{mRNA_codon} → {amino_acid}")

    return mRNA_codon, amino_acid


#Reading frames function
def reading_frames():
    dna_seq = get_dna_sequence()
    
    if not dna_seq or len(dna_seq) < 3:
        print("No valid DNA sequence provided.")
        return

    # Define complement bases
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Define strands
    strands = {
        "Coding (5'→3')": dna_seq,
        "Template (3'→5')": ''.join(complement.get(base, 'N') for base in reversed(dna_seq))
    }

    for strand_name, strand_seq in strands.items():
        print(f"\n{strand_name} strand reading frames:")

        if strand_name == "Coding (5'→3')":
            mrna_seq = strand_seq.replace('T', 'U')
        else:
            rna_complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
            mrna_seq = ''.join(rna_complement.get(base, 'N') for base in strand_seq)

        if 'N' in mrna_seq:
            print("Invalid mRNA sequence due to unknown bases.")
            continue

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


#For testing motif search function
def find_motif_positions(dna_seq, motif):
    #Returns a list of positions where the motif starts in the DNA sequence
    return [i for i in range(len(dna_seq)) if dna_seq.startswith(motif, i)]


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
    positions = find_motif_positions(dna_seq, motif)
    print(f"\nMotif '{motif}':")
    print(f"Found {count} time(s) at positions: {positions if positions else 'None'}")


# Mutation simulation function 
#For testing purposes, this function introduces random mutations into a DNA sequence
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


# Mutation simulation function- not for testing purposes, this function simulates mutations in a DNA sequence
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

    if num_mutations < 1 or num_mutations > len(dna_seq):
        print("Invalid number of mutations.")
        return

    mutated_seq, mutations = introduce_mutations(dna_seq, num_mutations)

    print("\nOriginal DNA sequence:")
    print(dna_seq)
    print("\nMutated DNA sequence:")
    print(mutated_seq)
    print("\nMutations introduced:")
    for pos, orig, new in mutations:
        print(f"Position {pos + 1}: {orig} → {new}")
