def to_rna(dna_strand):
    rna_dict = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    rna_strand = ""
    for i in dna_strand:
        if i in rna_dict:
            rna_strand += rna_dict[i]
    return rna_strand
