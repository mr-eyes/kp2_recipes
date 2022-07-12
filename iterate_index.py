import kProcessor as kp
from helper_functions import KFIter
import sys

kf = kp.kDataFrame.load("test_transcripts.fa_kf")

it = kf.begin()

while it != kf.end():
    kmer = it.getKmer()
    color = it.getColor()
    color_id = it.getColorID()
    color_by_color_id = kf.getColorByColorID(color_id)
    print(f"kmer({kmer}) colorID({color_id}) color({color})) colorByColorID({color_by_color_id})")
    it.next()

print("-------------------------------------------")

for color, count in kf.getColorHistogram().items():
    print(f"color({color}): count({count})")