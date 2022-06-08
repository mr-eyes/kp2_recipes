import kProcessor as kp
from helper_functions import KFIter
import sys

kf_prefix = sys.argv[1]

kf = kp.kDataFrame.load(kf_prefix)

with open(kf_prefix + "_exported.tsv", 'w') as op:
    for kmer_str, kmer_hash, kmer_count in KFIter(kf):
        op.write(f"{kmer_hash}\t{kmer_str}\t{kmer_count}\n")
