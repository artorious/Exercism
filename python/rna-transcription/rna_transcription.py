""" DNA transcription to RNA """


def to_rna(dna_strand):
    """ (str) -> str

        Performs DNA transcription to RNA given a DNA strand
        Returns RNA stand.
    """
    dna_to_rna_codec = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    if isinstance(dna_strand, str):
        dna_strand = dna_strand.strip()
        try:
            return ''.join([dna_to_rna_codec[x] for x in dna_strand])
        except KeyError as bad_key:
            raise ValueError(
                "Invalid DNA notation '{}'".format(bad_key.args[0]))
    else:
        raise TypeError('Expected string (DNA strand Notation)')
