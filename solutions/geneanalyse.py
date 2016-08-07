import fastaparse

def GC_skew (gene):
    """
    An important metric for analysing nucleotides is the GC skew,
    this gives a measure of the amount of guanine (G) compared to
    cytosine (C) in a gene sequence. This can be calculated by
    counting the number of each nucleotide and plugging that into
    the following equation (G-C)/(G+C), make sure to return as a
    float! 
    """
    gcount = gene["seq"].count("G")
    ccount = gene["seq"].count("C")
    return float(gcount - ccount)/(gcount + ccount)

def has_motif (gene, motif):
    """
    It can be helpful to know whether genes contain certain conserved
    patterns called motifs. This function should return a boolean
    True or False value dependant on whether a given motif string
    is found within the gene sequence.
    """
    return (motif in gene["seq"])

def analyse_gene (gene):
    """
    This function will take a gene entry and return a new dictionary
    with the following information.
    'gc_skew' -> the gc skew of the gene
    'tata_box' -> boolean for the presence of the motif "TATAAA"
    'ecor1' -> boolean for the presence of the motif "GAATTC"
    'cat_box' -> boolean for the presence of the motif "GGCCAATCT"
    """
    outdict = {}
    outdict["gc_skew"] = GC_skew(gene)
    outdict["tata_box"] = has_motif(gene, "TATAAA")
    outdict["ecor1"] = has_motif(gene, "GAATTC")
    outdict["cat_box"] = has_motif(gene, "GGCCAATCT")
    return outdict

def read_genes (fastafile):
    """
    This function will use the fastaparser to read genes from a
    specified opened file, analyse them and then return a list of
    analysed gene dictionaries.
    """
    output = []
    for entry in fastaparse.fasta_parser(fastafile):
        data_entry = analyse_gene(entry)
        output.append(data_entry)
    return output
