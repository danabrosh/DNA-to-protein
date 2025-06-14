from dna_functions import (
        codon_translation,
        reading_frames,
        motif_search,
        mutation_simulation,
        get_dna_sequence
    )


def main():
    print("Welcome to DNA to Protein!")
    print("Which function would you like to run?")
    print("1 - Codon Translation")
    print("2 - Reading Frames and ORFs")
    print("3 - Motif Search")
    print("4 - Mutation Simulation")
    choice = input("Enter the number the function you want to run: ")
    if choice == '1':
        try:
            dna_seq = get_dna_sequence()
            if dna_seq:  # Only proceed if we got a valid sequence
                codon_translation(dna_seq)
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '2':
        try:
            reading_frames()
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '3':
        try:
            motif_search()
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '4':
        try:
            mutation_simulation()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid. Please select 1-4 only.")

if __name__ == "__main__":
    main()
