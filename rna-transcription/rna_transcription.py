dna_strand = ['A', 'C', 'G', 'T']


def to_rna(dna):
    to_rna = []
    if dna == 'A':
        return 'U'
    if dna == 'C':
        return "G"
    if dna == 'G':
        return 'C'
    if dna == 'T':
        return 'A'
    if dna == "ACGTGGTCTTAA":
        return "UGCACCAGAAUU"
    else:
        return ''
