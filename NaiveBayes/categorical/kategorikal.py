class Categorical:
    def __init__(self,glucose,blood,bmi,age):
        if age >=20:
            self.glucose = glucose
            self.blood = blood
            self.bmi = bmi
            self.age = age
        else:
            print("sory, age must be older than 19 years")
    def Glucose(self):
        if self.glucose <=140:
            return "NORMAL"
        elif self.glucose >=141 and self.glucose <=199:
            return "PREDIABETES"
        elif self.glucose >=200:
            return "DIABETES"
        else:
            return "error"
    def Blood(self):
        if self.blood <=80:
            return "NORMAL"
        elif self.blood >=81 and self.blood <=89:
            return "PRAHIPERTENSI"
        elif self.blood >=90 and self.blood <=99:
            return "HIPERTENSI1"
        elif self.blood >=100 and self.blood <=199:
            return "HIPERTENSI2"
        elif self.blood >=120:
            return "KRISIS"
        else:
            return "error"

    def Bmi(self):
        if self.bmi <=18.5:
            return "KURANG"
        elif self.bmi >=18.6 and self.bmi <29.9:
            return "NORMAL"
        elif self.bmi >=30:
            return "OBESITAS"
        else:
            return "error"
    def Age(self):
        if self.age >=21 and self.age <=59:
            return "Dewasa"
        elif self.age >=60:
            return "Lansia"
        else:
            return "error"
