import kProcessor as kp
from helper_functions import KFIter
import sys

kSize = 21
kf1 = kp.kDataFrameFactory.createPHMAP(kSize)
kf2 = kp.kDataFrameFactory.createPHMAP(kSize)
seq1 = "CTTGGCTCACTGCAGCCTGCGCCTCCCTGGTTCAAGCGATTCTCCTGCCTTGGCCTCCAAGCAGCTGGGATTACAGGCGCCCGCCACCATGTCCTAATTTTTGTATTTTTAGAAGAGACGGGGTTTCACCATATGAGACAGGGTTTCA"
seq2 = "TCTTTTTTTTTTTGAGAAGGAGTTTCCCTCTTGTCACCCAGGTTGGGGTACAGGGGCGCTTTTTTGGCCCCCTGCAAACTCCGCTTCCTGGGTTCAAGGGATTCTCCTGCCTCAGCCCCCCGAGTAGCTGGAATTACAGGCCCCCCCC"
params = {"kSize": kSize}

kp.countKmersFromString(kf1, params, seq1)
kp.countKmersFromString(kf2, params, seq2)

kf1_kmers = set()
kf2_kmers = set()

for _, kmer_hash, _ in KFIter(kf1): kf1_kmers.add(kmer_hash)
for _, kmer_hash, _ in KFIter(kf2): kf2_kmers.add(kmer_hash)

kfs = kp.kFramesVector()
kfs.push_back(kf1)
kfs.push_back(kf2)



kf_union_kmers = set()
kf_union = kp.kFrameUnion(kfs)
print(f"size: {kf_union.size()}")

it = kf_union.begin()
while it != kf_union.end():
    kf_union_kmers.add(it.getHashedKmer())
    it.next()


kf_intersect_kmers = set()
kf_intersect = kp.kFrameIntersect(kfs)
it = kf_intersect.begin()
while it != kf_intersect.end():
    kf_intersect_kmers.add(it.getHashedKmer())
    it.next()

print(f"kf1_kmers({len(kf1_kmers)}) | kf2_kmers({len(kf2_kmers)}) | kf_union_kmers({len(kf_union_kmers)}) | kf_intersect_kmers({len(kf_intersect_kmers)})")