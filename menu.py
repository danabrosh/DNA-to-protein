# In this file, the user selects one of the dna_functions to run.
# The functions are imported from the dna_functions file.

#Import the functions from the dna_functions file
from dna_functions import (
        codon_translation,
        reading_frames,
        motif_search,
        mutation_simulation,
        get_dna_sequence)

#Main menu function to select which DNA function to run
def main():
    print("Welcome to DNA to Protein!")
    print("Which function would you like to run?")
    print("1 - Codon Translation")
    print("2 - Reading Frames and ORFs")
    print("3 - Motif Search")
    print("4 - Mutation Simulation")

    choice = input("Enter the number of the function you want to run: ")

    try:
        if choice == '1':
            dna_seq = get_dna_sequence()
            if dna_seq:
                codon_translation(dna_seq)
        elif choice == '2':
            reading_frames()
        elif choice == '3':
            motif_search()
        elif choice == '4':
            mutation_simulation()
        else:
            print("Invalid. Please select 1-4 only.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
