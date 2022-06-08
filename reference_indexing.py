import kProcessor as kp
from helper_functions import KFIter
import sys

kf = kp.kDataFrameFactory.createPHMAP(31)
filename = sys.argv[1]
chunk_size = 100
params = {"kSize": 31}
kp.index(kf, params, filename, chunk_size, filename + ".names")

kf.save(filename + "_kf")
