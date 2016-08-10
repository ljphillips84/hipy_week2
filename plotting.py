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
    n = 0
    for entry in dict_list:
        if entry[testing_key] == True:
            n +=1
    return n

def bar_graph(high_data, low_data, categories):
    '''
    Plots a bar graph of the proportion of each dataset in each category
    in this case being the proportion of each dataset containing each
    motif. Should include labels for different categories, and have
    both dataseries plotted side-by-side for easy analysis.
    '''

    high_data_prop = []
    low_data_prop = []

    for point in high_data:
        high_data_prop.append(point/sum(high_data))
    for point in low_data:
        low_data_prop.append(point/sum(low_data))

    fig, ax = plt.subplots()

    index = np.arange(len(motifs))
    bar_width = 0.35

    opacity = 0.4

    rects1 = plt.bar(index, high_data_prop, bar_width,
                     alpha=opacity,
                     color='b',
                     label='High')

    rects2 = plt.bar(index + bar_width, low_data_prop, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Low')

    plt.xlabel('Motifs')
    plt.ylabel('Proportion of proteins containing the motif')
    plt.title('Incidence of matching motifs, high vs. low')
    plt.xticks(index + bar_width, (motifs))
    plt.legend()

    plt.tight_layout()
    plt.show()
    return

with open("high.fasta", "r") as high_genes:
    high_info = geneanalyse.read_genes(high_genes)

with open("low.fasta", "r") as low_genes:
    low_info = geneanalyse.read_genes(low_genes)

# skew_box_plots([i["gc_skew"] for i in high_info],
#                [i["gc_skew"] for i in low_info],
#                save_loc="testing.png")
motifs = ["tata_box", "ecor1", "cat_box"]

#bar_graph(high_info, low_info, motifs)

high_data = []
for motif in motifs:
    high_data.append(number_true(high_info,motif))
    #print(motif+" : "+str(number_true(high_info,motif)))

low_data = []
for motif in motifs:
    low_data.append(number_true(low_info,motif))
    #print(motif+" : "+str(number_true(low_info,motif)))

bar_graph(high_data,low_data,motifs)