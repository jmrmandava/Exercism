def to_rna(dna):
    a = {'A': 'U',
         'C': 'G',
         'G': 'C',
         'T': 'A'}

    b = ''

    for i in dna:
        b += a.get(i)
    return b
