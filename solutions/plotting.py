import matplotlib.pyplot as plt
import numpy as np
import geneanalyse

def skew_box_plots(high_data, low_data, save_loc=False):
    '''
    Takes two lists of numerical data, and plots a box plot
    of both of them using numpy and matplotlib, optionally
    writes to a save location instead of displaying.
    '''
    combined_data = [high_data, low_data]
    plt.boxplot(combined_data)
    if save_loc == False:
        plt.show()
    else:
        plt.savefig(save_loc)
    return
    
def number_true(dict_list, testing_key):
    '''
    Returns the number of entries in a given list of
    dictionaries that have True as the value for a given
    key.
    '''
    return len(filter(lambda i: i[testing_key], dict_list))

def bar_graph(high_data, low_data, categories):
    '''
    Plots a bar graph of the proportion of each dataset in each category
    in this case being the proportion of each dataset containing each
    motif. Should include labels for different categories, and have
    both dataseries plotted side-by-side for easy analysis.
    '''
    high_values = []
    low_values = []
    for category in categories:
        high_values.append(float(number_true(high_data, category))
                           /len(high_data))
        low_values.append(float(number_true(low_data, category))
                          /len(low_data))
    ind = np.arange(len(categories))
    fig, ax = plt.subplots()
    high_rects = ax.bar(ind, high_values, 0.35, color='r')
    low_rects = ax.bar(ind+0.35, low_values, 0.35, color='g')
    labels = [categories[i/2] if i%2 else "" for i in xrange(6)]
    ax.set_xticklabels(labels)
    plt.show()
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
