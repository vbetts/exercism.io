def to_rna(dna_strand):
    rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
    result = ""
    for n in dna_strand:
        if n in rna:
            result += rna[n]
        else:
            raise Exception("ValueError: " + n + " is not a valid nucleotide.")
    return result
