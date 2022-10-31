class Drib:
    def __init__(self, chis_par, znam_par):
        self.chis = chis_par
        self.znam = znam_par

    def __str__(self):
        return f"{self.chis}, {self.znam}"

    def dod(self):
        return f"{self.chis + self.znam}"

    def vid(self):
        return f"{self.chis - self.znam}"

    def mnoge(self):
        return f"{self.chis * self.znam}"

    def dil(self):
        if self.znam != 0:
            return f"{self.chis / self.znam}"
        else:
            return f"ne deli na nol"

    def reload(self, chis, znam):
        self.chis = chis
        self.znam = znam
        return f"Zameneno"



result = Drib(chis_par=10, znam_par=15)

print(result.dod())
print(result.vid())
print(result.reload(1, 3))
print(result)

