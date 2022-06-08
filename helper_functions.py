import kProcessor as kp


class KFIterator:
    def __init__(self, KF):
        self.KF = KF.kf
        self.it = KF.kf.begin()
        self.end = KF.kf.end()

    def __next__(self):

        if self.it != self.end:
            kmer_str = self.it.getKmer()
            kmer_hash = self.it.getHashedKmer()
            kmer_count = self.it.getCount()
            kmer = (kmer_str, kmer_hash, kmer_count)
            self.it.next()
            return kmer

        else:
            raise StopIteration


class KFIter:
    def __init__(self, KF):
        self.kf = KF

    def __iter__(self):
        return KFIterator(self)
