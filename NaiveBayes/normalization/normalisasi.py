import numpy as np
class Normalization:
    def __init__(self,glukosa,darah,berat,umur,label,total):
        self.glukosa = glukosa
        self.darah = darah
        self.berat = berat
        self.umur = umur
        self.label = label
        self.total = total
    def Outcome(self):
        Glucose = self.glukosa / self.label
        Blood = self.darah / self.label
        Bmi = self.berat / self.label
        Age = self.umur / self.label
        label = self.label / self.total
        result = np.float32(Glucose * Blood * Bmi * Age * label )
        return result
