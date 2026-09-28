from modules.sequence import *
from modules.analysis import *

def get_dna():
    s = input("Enter DNA sequence: ").upper().replace(" ", "")
    if not validate_sequence(s):
        raise ValueError("Use only A, C, G and T.")
    return s

def sequence_lab():
    while True:
        print("\n=== DNA SEQUENCE LAB ===")
        print("1 Validate  2 Count  3 GC%  4 Reverse  5 Complement")
        print("6 Reverse Complement  7 Summary  8 Back")
        c = input("Choose: ").strip()
        if c == "8": return
        try:
            s = get_dna()
            if c == "1": print("Valid DNA sequence.")
            elif c == "2": print("Counts:", nucleotide_count(s))
            elif c == "3": print(f"GC content: {gc_content(s):.2f}%")
            elif c == "4": print("Reverse:", reverse_sequence(s))
            elif c == "5": print("Complement:", complement_sequence(s))
            elif c == "6": print("Reverse complement:", reverse_complement(s))
            elif c == "7": print_summary(s)
            else: print("Invalid choice.")
        except ValueError as e: print("Input error:", e)

def print_summary(s):
    x = sequence_summary(s)
    print("\n=== DNA SUMMARY ===")
    for k, v in x.items(): print(f"{k.replace('_',' ').title()}: {v}")

def analysis_lab():
    while True:
        print("\n=== DNA ANALYSIS LAB ===")
        print("1 DNA→RNA  2 RNA→Protein  3 Find Motif  4 Compare Sequences  5 Back")
        c = input("Choose: ").strip()
        try:
            if c == "5": return
            if c == "1": print("RNA:", transcribe_dna(get_dna()))
            elif c == "2":
                r = input("Enter RNA (A,U,C,G): ").upper().replace(" ","")
                print("Protein:", translate_rna(r))
            elif c == "3":
                s = get_dna()
                m = input("Motif: ").upper().replace(" ","")
                print("Positions:", find_motif(s, m) or "Not found")
            elif c == "4":
                a, b = get_dna(), get_dna()
                print(compare_sequences(a,b))
            else: print("Invalid choice.")
        except ValueError as e: print("Input error:", e)

def main():
    while True:
        print("\n" + "="*48)
        print("                 DNA ANALYSER")
        print("      Interactive DNA Sequence Analysis Lab")
        print("="*48)
        print("1 DNA Sequence Lab")
        print("2 DNA Analysis Lab")
        print("3 Bio Quiz Lab")
        print("4 Exit")
        c = input("Choose: ").strip()
        if c == "1": sequence_lab()
        elif c == "2": analysis_lab()
        elif c == "3": run_quiz()
        elif c == "4": break
        else: print("Invalid choice.")

if __name__ == "__main__": main()
