from modules.sequence import req,nucleotide_count,gc_content,at_content,complement_sequence,reverse_complement

RNA_COMP={"A":"U","T":"A","C":"G","G":"C"}
CODONS={"AUG":"M","UUU":"F","UUC":"F","UUA":"L","UUG":"L","UAA":"*","UAG":"*","UGA":"*","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GGU":"G","GGC":"G","GGA":"G","GGG":"G"}

def transcribe_dna(s): return "".join(RNA_COMP[b] for b in req(s))

def translate_rna(r):
    r=r.upper().replace(" ","")
    if not r or not set(r).issubset(set("AUCG")): raise ValueError("Invalid RNA sequence.")
    out=[]
    for i in range(0,len(r)-2,3):
        aa=CODONS.get(r[i:i+3], "?")
        if aa=="*": break
        out.append(aa)
    return "-".join(out) if out else "No complete codons translated."

def find_motif(s,m):
    s=req(s); m=req(m); out=[]; start=0
    while True:
        i=s.find(m,start)
        if i<0: return out
        out.append(i+1); start=i+1

def compare_sequences(a,b):
    a,b=req(a),req(b); n=min(len(a),len(b))
    matches=sum(a[i]==b[i] for i in range(n))
    return {"length_1":len(a),"length_2":len(b),"matches":matches,
            "mismatches":n-matches,"similarity":(matches/n*100 if n else 0)}

def sequence_summary(s):
    s=req(s); d=nucleotide_count(s)
    return {"length":len(s),"A":d["A"],"C":d["C"],"G":d["G"],"T":d["T"],
            "gc_content":round(gc_content(s),2),"at_content":round(at_content(s),2),
            "complement":complement_sequence(s),"reverse_complement":reverse_complement(s)}

def run_quiz():
    from modules.quiz import run_quiz as rq
    rq()
