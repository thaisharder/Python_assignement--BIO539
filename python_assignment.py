import pandas as pd
import sys
import plotnine as p9


def sequence_select(filename):
    """
    Summary
    Reads a specific file with an imput filename and as a result will creat a string

    Parameters
    filename: will sequence the filename as a string

    Return
    string: the whole sequence as a file
    """
    with open (filename, 'r') as seq_file:
        text = seq_file.read()
    return(text)


def counting_kmers(seq, k):
    """
    Summary
    Counting kmers occurrence in a given read.

    Parameters
    seq: string
    k : int. Indicates the size of the kmers

    Returns
    count_k_dct: counts the number of kmers from a dictionary that countains all the unique kmers
    """
    assert k > 0, "Please, specify k > 0"
    assert k <= len(seq), "Please, specify k smaller or equal to length of the sequence"
    count_k_dct = {}
    num_kmers = len(seq) - k + 1
    for x in range(num_kmers):
        kmer = seq[x:x+k]
        if kmer not in count_k_dct:
            count_k_dct[kmer] = 0
        count_K_dict[kmer] += 1
    return count_k_dct


def pdframe_kmers(seq):
    """
    Sumary
    This function will create a dataframe that contains possible kmers and observed kmers
    from a specific sequence

    Parameters
    seq: string
    k : int. Indicates the size of the kmers

    Returns
    dataframe: a dictionary with observed kamers and possible kmers for each value given for k
    """
    K_obs = []
    for kmers_obs in range(1,len(seq)+1):
        kmers_obs_dct = {}
        all_kmers = len(seq) - kmers_obs + 1
        for x in range(all_kmers):
            kmers = seq[x:x+kmers_obs]
            if kmers not in kmers_obs_dct:
                kmers_obs_dct [kmers] = 0
            kmers_obs_dct[kmers] += 1
        k_obs.append(len(kmers_obs_dct))

    K_pos = []
    for w in range(1,len(seq)+1):
        if (len(seq) - w + 1) > (4**w):
            k_pos.append(4**w)
        else:
            k_pss.append(len(seq) - w + 1)
    k = list(range(1,len(seq)+1))
    K_pos_dct = {'k':k, 'k_observed':k_obs, 'k_possible':K_pos}
    return pdframe_kmers

    import pandas as pd
    pdframe_kmers = pd.DataFrame(obs_poss_dct, columns = ['k','kmers_obs', 'kmers_poss'])
    return pdframe_kmers


def plots(pdframe_kmers, filename):

    """
    Creating a graph with the proportion of kmers oberserved.
    This function will creat a plot based on oberserved kmers using the
    dataframe that was created before.
    """
    proportion_kmers_oberserved = p9.ggplot(data = pdframe_kmers_df,
                                           mapping = p9.aes(x = 'k' , y = 'kemers_obs/kmers_poss')) + p9.geom_point()

    proportion_kmers_oberserved.save(filename + "proportion_kmers_oberserved.pdf")



def linguistic_complexity(seq):

    """
    Summary: this code will calculate the lingustic complexity (observred kemers/possible kemrs) of a sequence.

    Parameters
    seq: stirng

    Return
    dataframe:
    """

    assert seq != '', "please, specify a valid sequence (not empty)"
    K_obs = []
    for kmers_obs in range(1,len(seq)+1):
        kmers_obs_dct = {}
        all_kmers = len(seq) - kmers_obs + 1
        for x in range(all_kmers):
            kmers = seq[x:x+kmers_obs]
            if kmers not in kmers_obs_dct:
                kmers_obs_dct [kmers] = 0
            kmers_obs_dct[kmers] += 1
        k_obs.append(len(kmers_obs_dct))

    K_pos = []
    for w in range(1,len(seq)+1):
        if (len(seq) - w + 1) > (4**w):
            k_pos.append(4**w)
        else:
            k_pss.append(len(seq) - w + 1)
    k = list(range(1,len(seq)+1))
    K_pos_dct = {'k':k, 'k_observed':k_obs, 'k_possible':K_pos}
    return pdframe_kmers
    import pandas as pd
    pdframe_kmers = pd.DataFrame(obs_poss_dct, columns = ['k','kmers_obs', 'kmers_poss'])

    observed = pdframe_kmers['kmers_obs'].sum()
    possible = pdframe_kmers['kmers_poss'].sum()
    linguistic_complexity = observed/possible
    return linguistic_complexity


    if __name__ == '__main__':
        myfile = sys.argv[1]
        myseq = sequence_select(myfile)
        my_kmers_df = pdframe_kmers(myseq)
        my_linguistic_complexity = linguistic_complexity(myseq)
        print(my_kmers_df)
        print('The linguistic complexity is', my_linguistic_complexity)
        make_plots(my_kmers_df,myfile)
    
