def get_name(header):
    '''
    Takes a header string and returns the region between the header
    marker and the first space. I.e :
    >gi|3641541|gb|AF073518.1| Homo sapiens small EDRK-rich facto...
    returns
    gi|3641541|gb|AF073518.1|
    '''
    return


def fasta_parser(pFile):
    '''
    Generator, reads from opened fasta file and yields dictionaries
    with the following fields.
       'seq' -> full DNA sequence
       'name' -> result of get_name above
    Lines starting with > are headers, signalling new sequence
    records.
    Lines starting with ; are comments, which should be skipped.
    For more help, see hints file.
    '''
    yield


            
            
