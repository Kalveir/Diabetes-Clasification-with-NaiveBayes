class Compare:
    def __init__(self,positif,negatif):
        self.negatif = negatif
        self.positif = positif
    def Output(self):
        if self.negatif > self.positif :
            return "Negative"
        else:
            return"Positive"
