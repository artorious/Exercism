""" DNA transcription to RNA """


def to_rna(dna_strand):
    """ (str) -> str

        Performs DNA transcription to RNA given a DNA strand
        Returns RNA stand.
    """
    if isinstance(dna_strand, str):
        dna_strand = dna_strand.upper().strip()
        dna_strand_set = set(dna_strand)
        rna_strand = ''

        if dna_strand_set.issubset(set('ACGT')):
            for a_letter in dna_strand:
                if a_letter == 'A':
                    rna_strand += 'U'
                elif a_letter == 'C':
                    rna_strand += 'G'
                elif a_letter == 'G':
                    rna_strand += 'C'
                elif a_letter == 'T':
                    rna_strand += 'A'
            return rna_strand
        else:
            raise ValueError('Invalid DNA strand')
    else:
        raise TypeError('Expected string (DNA strand Notation)')
