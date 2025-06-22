# DNA-to-protein


Proteins are essential molecules responsible for most of the work inside our cells-support structure, enable biochemical reactions, transport substances, and regulate processes.
The genetic information that cells use to build new proteins is stored in the DNA.
To use this information, cells perform two key steps: 
1. **Transcription** – the DNA is copied into messenger RNA (mRNA).
2. **Translation** – the mRNA is read in sets of three bases called **codons**, each coding for a specific amino acid.
   
## What does this project do? 

This project simulates how cells turn DNA into proteins through transcription and translation. It includes four main parts:

1. **Codon Translation**  
   Converts a 3-letter DNA codon (like ATG) to its mRNA complement (UAC) and then translates it into the corresponding amino acid (Tyrosine).
2. **Reading Frames and ORFs**  
   Analyzes a full DNA sequence, prints all three reading frames, finds valid open reading frames (from `AUG` to a stop codon), and translates them. Repeats for the complementary strand.
3. **Motif Search**
   Searches the sequence for known or user-defined motifs (for example,TATA, CG) and reports how many times they appear and their positions.
4. **Mutation Simulation**  
   Introduces random point mutations and shows the mutated sequence with differences- can serve as a biological tool for exploring gene variation.
## Input:
 The user is prompted to provide the DNA sequence either by entering it manually or by loading it from a FASTA file through an interactive menu.
 
 • The user will be asked to choose which function to run (Codon Translation, Reading Frames, Motif Search, or Mutation Simulation).  
- Depending on the part:
  - A codon (3 letters) for translation
  - A DNA sequence (≥3 bases) for reading frames
  - A motif (predefined or custom)
  - Number of mutations to introduce
## Output:
- RNA codons and amino acids  
- Reading frames and translated proteins  
- Motif counts and positions  
- Mutated DNA with listed base changes

 ## 🧪 Running Examples
 **Codon Translation** 
 - Input: ATG
 - Output: mRNA codon: UAC, UAC → Tyrosine
   **Reading Frames and ORFs**
   - Input: ATGGGCTTTTAA
   - Output: Frame 1: AUG → Methionine, GGC → Glycine, UUU → Phenylalanine, UAA → STOP. Frame 2: No start codon (AUG) found. Frame 3: No start               codon (AUG) found.
           Template (3'→5') strand reading frames: Frame 1: No start codon (AUG) found. Frame 2: No start codon (AUG) found. Frame 3:No                     start codon (AUG) found.
   **Motif Search**
   - Input: TATACGAATAAATTAGGGCAG, motif- TATA.
   - Output: Motif 'TATA': Found 1 time(s) at positions: [0].
   **Mutation Simulation**
   - Input: ATGCGTACG. Number of mutations: 3.
   - Output: Mutated DNA sequence: ATGCGAATA. Mutations introduced: Position 6: T → A,  Position 8: C → T, Position 9: G → A.

## 🗂️ Project Structure
This project contains 4 files-
1. **menu.py** – Contains the main function, which displays a menu. The user selects which function to run and provides a DNA sequence.
2. **dna_functions.py**– Contains the main biological functions and helper functions for tasks like transcription, translation, motif search,                            and mutation simulation.
3. **test_dna_functions.py**– Includes basic tests for the main functions to make sure they return correct results using sample DNA sequences.
4. **requirements.txt** – Currently empty, as the project doesn't use external libraries beyond Python’s built-in modules

## ⚙️ How to Use
  * This project is written in Python 3.

    Run the following commands in your terminal:
  ```bash
git clone https://github.com/danabrosh/dna-to-protein.git
cd dna-to-protein
pip install -r requirements.txt
python menu.py
```

---

This project was created as part of [Basic Programming Skills (Python)](https://github.com/Code-Maven/wis-python-course-2025-03) course at the Weizmann Institute of Science.



