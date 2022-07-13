from typing import List
import kProcessor as kp
import sys


def upsetPlot(genomeFileNames):
    genomes_kframes = kp.kFramesVector()
    for _genome in genomeFileNames:
        genomes_kframes.push_back(kp.kDataFrame.load(_genome))

    kSize = genomes_kframes[0].getkSize()
    kframe = kp.kDataFrameFactory.createPHMAP(kSize)
    kp.indexPriorityQueue(genomes_kframes, "", kframe)
    colorsCounts = kframe.getColorHistogram()

    for colorID, colorCount in colorsCounts.items():
        colors = kframe.getColorByColorID(colorID)
        print(genomeFileNames[colors[0]])
        for color in colors:
            print(f"& {genomeFileNames[color]}")

        print(f"= {colorCount/1000}")


def main():
    if len(sys.argv) < 3:
        sys.exit("run: python upset.py <kDataframes ...>")
    genomesFileNames = sys.argv[1:]
    upsetPlot(genomesFileNames)


if __name__ == "__main__":
    main()
