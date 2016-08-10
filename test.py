import fastaparse

fastafile = open('data.txt','r')

my_parser = fastaparse.fasta_parser(fastafile)

for gene in my_parser:
    print(gene['name']+" : "+gene['seq'])

# geneblocks = []
# gene = ["",""]
# n = 0
#
# for line in fastafile.read().split("\n"):
#     if line != "":
#         if line[0] == ">":
#             if n == 1:
#                 geneblocks.append(gene)
#                 gene = ["",""]
#             gene[0] = fastaparse.get_name(line)
#         else:
#             n = 1
#             gene[1] = str(gene[1]) + line
#
# geneblocks.append(gene)
#
# for protein in geneblocks:
#     print(protein)
#     if "TATAAA" in protein[1]:
#         print(True)
#     else:
#         print(False)
#     if "GAATTC" in protein[1]:
#         print(True)
#     else:
#         print(False)
#     if "GGCCAATCT" in protein[1]:
#         print(True)
#     else:
#         print(False)