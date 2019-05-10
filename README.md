# Python assignment 

## Goal
This repository contains a script that will calculate the linguistic complexity of a specific string. LInguistic complexity can be calculated based on the proportion of k-mers that are observed compared to the total number that are theoretically possible.
The script contains five functions:

sequence_select
This function will read a specific file with an imput filename and, as a result, will creat a string. The file that contains the sequence should be specified here as an argument. 

Counting_kmers
This function will calculate the occurance of k-mers in a specific sequence (read)

pdframe_kmers
This function will create a dataframe (similiar to a table) that contains possible k-mers and observed k-mers from a specific sequence.
K_obs = observed kmers
k_pos = possible kmers 
To creat the dataframe it is necessary to "import panda as pd" by the end of the function.

plots
After generate a dataframe this script will create graphs based on observed k-mers/possible k-mers (y-axes) and a specific k (x-axes) 

liguistic_complexity
This function will generate a number that represents the lingusitic complexity, which is the result of the division of "observed kemrs" by "possible kmers" given a specific sequence. 

This repository also contians 
