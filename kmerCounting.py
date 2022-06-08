import kProcessor as kp
from helper_functions import KFIter
import sys

kf = kp.kDataFrameFactory.createPHMAP(31)
filename = sys.argv[1]
chunk_size = 100
params = {"kSize": 31}
kp.countKmersFromFile(kf, params, filename, chunk_size)

with open(filename + ".count", 'w') as op:
    for kmer_str, kmer_hash, kmer_count in KFIter(kf):
        op.write(f"{kmer_hash}\t{kmer_str}\t{kmer_count}\n")