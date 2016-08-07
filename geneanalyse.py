import fastaparse

def GC_skew (gene):
    '''
    An important metric for analysing nucleotides is the GC skew,
    this gives a measure of the amount of guanine (G) compared to
    cytosine (C) in a gene sequence. This can be calculated by
    counting the number of each nucleotide and plugging that into
    the following equation (G-C)/(G+C), make sure to return as a
    float!
    '''
    return

def has_motif (gene, motif):
    '''
    It can be helpful to know whether genes contain certain conserved
    patterns called motifs. This function should return a boolean
    True or False value dependant on whether a given motif string
    is found within the gene sequence.
    '''
    return

def analyse_gene (gene):
    '''
    This function will take a gene entry and return a new dictionary
    with the following information.
    'gc_skew' -> the gc skew of the gene
    'tata_box' -> boolean for the presence of the motif "TATAAA"
    'ecor1' -> boolean for the presence of the motif "GAATTC"
    'cat_box' -> boolean for the presence of the motif "GGCCAATCT"
    '''
    return

def read_genes (fastafile):
    '''
    This function will use the fastaparser to read genes from a
    specified opened file, analyse them and then return a list of
    analysed gene dictionaries.
    '''
    return 
