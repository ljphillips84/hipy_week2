import matplotlib.pyplot as plt
import numpy as np
import geneanalyse

def skew_box_plots(high_data, low_data, save_loc=False):
    '''
    Takes two lists of numerical data, and plots a box plot
    of both of them using numpy and matplotlib, optionally
    writes to a save location instead of displaying.
    '''
    return
    
def number_true(dict_list, testing_key):
    '''
    Returns the number of entries in a given list of
    dictionaries that have True as the value for a given
    key.
    '''
    return

def bar_graph(high_data, low_data, categories):
    '''
    Plots a bar graph of the proportion of each dataset in each category
    in this case being the proportion of each dataset containing each
    motif. Should include labels for different categories, and have
    both dataseries plotted side-by-side for easy analysis.
    '''
    return

with open("high.fasta", "r") as high_genes:
    high_info = geneanalyse.read_genes(high_genes)

with open("low.fasta", "r") as low_genes:
    low_info = geneanalyse.read_genes(low_genes)

skew_box_plots([i["gc_skew"] for i in high_info],
               [i["gc_skew"] for i in low_info],
               save_loc="testing.png")
motifs = ["tata_box", "ecor1", "cat_box"]
bar_graph(high_info, low_info, motifs)
