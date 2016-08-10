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
    C = 0.0
    G = 0.0
    for i in gene:
        if i == 'C':
            C += 1.0
        elif i == 'G':
            G += 1.0

    return(G-C)/(G+C)

def has_motif (gene, motif):
    '''
    It can be helpful to know whether genes contain certain conserved
    patterns called motifs. This function should return a boolean
    True or False value dependant on whether a given motif string
    is found within the gene sequence.
    '''
    if motif in gene:
        test = True
    else:
        test = False
    return test

def analyse_gene (gene):
    '''
    This function will take a gene entry and return a new dictionary
    with the following information.
    'gc_skew' -> the gc skew of the gene
    'tata_box' -> boolean for the presence of the motif "TATAAA"
    'ecor1' -> boolean for the presence of the motif "GAATTC"
    'cat_box' -> boolean for the presence of the motif "GGCCAATCT"
    '''

    gene_analysis = {}

    gene_analysis['gc_skew'] = GC_skew(gene['seq'])
    gene_analysis['tata_box'] = has_motif(gene['seq'],'TATAAA')
    gene_analysis['ecor1'] = has_motif(gene['seq'], 'GAATTC')
    gene_analysis['cat_box'] = has_motif(gene['seq'], 'GGCCAATCT')

    return gene_analysis

def read_genes (fastafile):
    '''
    This function will use the fastaparser to read genes from a
    specified opened file, analyse them and then return a list of
    analysed gene dictionaries.
    '''

    my_parser = fastaparse.fasta_parser(fastafile)

    genes = []

    for protein in my_parser:
        genes.append(analyse_gene(protein))
    return genes