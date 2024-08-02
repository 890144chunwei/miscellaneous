# DNA Toolkit file
import collections
DNA_nuc = ["A", "T", "C", "G"]
RNA_nuc = ["A", "U", "C", "G"]

# Validate DNA sequencings
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for base in tmpseq:
        if base not in DNA_nuc:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreDict = {"A": 0, "T": 0, "C":0, "G":0}
    for base in seq:
       tmpFreDict[base] += 1
    return tmpFreDict
    #return dict(collections.Counter(seq))

