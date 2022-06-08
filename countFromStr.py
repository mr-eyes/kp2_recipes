import kProcessor as kp
from helper_functions import KFIter
import sys

kf = kp.kDataFrameFactory.createPHMAP(31)
seq = "CTTGGCTCACTGCAGCCTGCGCCTCCCTGGTTCAAGCGATTCTCCTGCCTTGGCCTCCAAGCAGCTGGGATTACAGGCGCCCGCCACCATGTCCTAATTTTTGTATTTTTAGAAGAGACGGGGTTTCACCATATGAGACAGGGTTTCA"
params = {"kSize": 31}

kp.countKmersFromString(kf, params, seq)

for kmer_str, kmer_hash, kmer_count in KFIter(kf):
    print(f"{kmer_hash}\t{kmer_str}\t{kmer_count}")