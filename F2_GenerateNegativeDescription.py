import os
from pathlib import Path


class GenerateNegativeDescriptionFile:
    def __init__(self, dec_minW, dec_minH, numPos, numNeg, numStages):
        self.dec_minW = dec_minW
        self.dec_minH = dec_minH
        self.numPos = numPos
        self.numNeg = numNeg
        self.numStages = numStages
        self.rootpath = Path(__file__).parent

    def create_txt_file(self):
        with open("neg.txt", "w") as f:
            [f.write("negative/" + filename.name + "\n") for filename in (self.rootpath / "n").iterdir()]

        with open("pos.txt", "w") as f:
            [f.write("positive/" + filename.name + "\n") for filename in (self.rootpath / "p").iterdir()]

    def define_roi(self):
        command = rf"{self.rootpath}\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images={self.rootpath}\p"
        os.system(command)

    def create_samples(self):
        command = rf"{self.rootpath}\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info {self.rootpath}\pos.txt -w {self.dec_minW} -h {self.dec_minW} -num {self.numNeg} -vec pos.vec"
        os.system(command)

    def train_model(self):
        command = rf"{self.rootpath}\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -precalcValBufSize 3000 -precalcIdxBufSize 3000 -minHitRate 0.999 -maxFalseAlarmRate 0.3 -vec pos.vec -bg neg.txt -w {self.dec_minW} -h {self.dec_minW} -numPos {self.numPos} -numNeg {self.numNeg} -numStages {self.numStages}"
        os.system(command)


if __name__ == "__main__":
    # train.Play()
    gnd = GenerateNegativeDescriptionFile(dec_minW=24, dec_minH=24, numPos=110, numNeg=1000, numStages=12)
    # gnd.create_txt_file()  # 01
    # gnd.define_roi()  # 02
    # gnd.create_samples()  # 03
    # gnd.train_model()  # 04
