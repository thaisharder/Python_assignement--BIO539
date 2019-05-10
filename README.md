# Python assignment 

## Instructions 
This repository contains a script ("python_assignment.py" and the markdown version of it "python_assignment_MKD") that will calculate the linguistic complexity of a specific string (see short string example in test_seq.txt). Linguistic complexity can be calculated based on the proportion of k-mers that are observed compared to the total number that is theoretically possible. The repository also has a script (test_python_assignment.py) to test the functions wrote on "python_assignment.py".

NOTE1: To run this script it is necessary that "python_assignment.py", the sequence that it is being tested, and the "test_python_assignment.py" are all in the same directory. To test the script before running it, one should access the command line and change to the directory where all three documents are. Next, one should type "py.test". If the script works properly, a message saying the test passed will appear. After that, one can type "python python_assignment.py" and the script should run.

NOTE2: python command didn't work on my command line (Git bash). I tried to use Anaconda but I also had an error message saying "DeprecationWarning: `formatargspec` is deprecated since Python 3.5. Use `signature` and the `Signature` object directly". Because of that, I couldn't run the "test_python_assignment.py". 

The script contains five functions:

sequence_select: this function will read a specific file with an input filename and, as a result, will creat a string. The file that contains the sequence should be specified here as an argument. 

Counting_kmers: this function will calculate the occurence of k-mers in a specific sequence (read)

pdframe_kmers: this function will create a dataframe (similar to a table) that contains possible k-mers and observed k-mers from a specific sequence.
K_obs = observed kmers
k_pos = possible kmers 
To create the dataframe it is necessary to "import panda as pd" by the end of the function.

plots: after generating a dataframe this script will create graphs based on observed k-mers/possible k-mers (y-axes) and a specific k (x-axes) 

liguistic_complexity: this function will generate a number that represents the linguisitic complexity, which is the result of the division of "observed kmers" by "possible kmers" given a specific sequence. 
