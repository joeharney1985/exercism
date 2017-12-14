mapping = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna_strand):
    try:
        return ''.join(mapping[c] for c in dna_strand)
    except KeyError as e:
        raise ValueError('invalid input.')sdf
