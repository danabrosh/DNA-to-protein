# DNA-to-protein-
## 🔬 What does this project do?

This project simulates how cells turn DNA into proteins through transcription and translation. It includes four main parts:
1. **Codon Translation**  
   Converts a 3-letter DNA codon (like `ATG`) into an RNA codon and then translates it into the corresponding amino acid.
2. **Reading Frames and ORFs**  
   Analyzes a full DNA sequence (text or FASTA), prints all three reading frames, finds valid open reading frames (from `AUG` to a stop codon),     and translates them. Repeats for the complementary strand.
3. **Motif Search**
   Searches the sequence for known or user-defined motifs (`TATA`, `CG`) and reports how many times they appear and their positions.
4. **Mutation Simulation**  
   Introduces random point mutations and shows the mutated sequence with differences.

   ## 📥 Input and Output
### Input:
 DNA sequence as a string or a FASTA file.
- Depending on the task:
  - A codon (3 letters)
  - A motif (predefined or custom)
  - Number of mutations to introduce
### Output:
- RNA codons and amino acids  
- Reading frames and translated proteins  
- Motif counts and positions  
- Mutated DNA with listed base changes
  
## ⚙️ How to Use
   git clone https://github.com/danabrosh/dna-to-protein.git  
   cd dna-to-protein
   pip install -r requirements.txt



## This project was created as part of the course Basic Programming Skills (Python) at the Weizmann Institute of Science.



