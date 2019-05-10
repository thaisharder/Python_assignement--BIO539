from python_assignment import *
import pytest


def test_counting_kmers():
    sequence = "ATTTGGATT" #example of sequence
    k = 3
    expected_output = {'ATT': 2, 'TTT': 1, 'TTG': 1, 'TGG': 1, 'GGA': 1, 'GAT': 1}
    assert expected_output == test_counting_kmers (sequence,k)



def test_pdframe_kmers():
    sequence = "ATTTGGATT" #example of sequence
    expeced_output = [3,5,6,6,5,4,3,2,1]
    assert  expected_output == test_pdframe_kmers (expeced_output)


def test_pdframe_kmers():
    sequence = "ATTTGGATT"
    expected_output = {'k':[1,2,3,4,5,6,7,8,9], 'kmers_obs':[3,5,6,6,5,4,3,2,1], 'kmers_poss':[4,8,7,6,5,4,3,2,1]}
    assert expected_output == test_pdframe_kmers(expected_output)


def test_linguistic_complexity():
    sequence = "ATTTGGATT"
    expected_output = 0.875
    assert expected_output == test_linguistic_complexity(sequence)
