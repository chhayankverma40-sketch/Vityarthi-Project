BASES=set("ACGT")
COMP={"A":"T","T":"A","C":"G","G":"C"}

def clean_sequence(s): return s.upper().replace(" ","").replace("\n","")
def validate_sequence(s): return bool(s) and set(s).issubset(BASES)

def req(s):
    s=clean_sequence(s)
    if not validate_sequence(s): raise ValueError("Invalid DNA sequence.")
    return s

def nucleotide_count(s):
    s=req(s); d={b:0 for b in "ACGT"}
    for b in s: d[b]+=1
    return d

def gc_content(s):
    d=nucleotide_count(s); return (d["G"]+d["C"])/len(req(s))*100

def at_content(s):
    d=nucleotide_count(s); return (d["A"]+d["T"])/len(req(s))*100

def reverse_sequence(s): return req(s)[::-1]
def complement_sequence(s): return "".join(COMP[b] for b in req(s))
def reverse_complement(s): return complement_sequence(s)[::-1]
