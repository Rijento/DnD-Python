class Armor(object):
    def __init__(self,name,weight,AC):
        self.name = name
        self.weight = weight
        self.AC = AC
    def getArmorName(self):
        return self.name
    def getArmorWeight(self):
        return self.weight
    def getArmorAC(self):
        return self.AC



armorPadded = Armor('Padded Armor','light',11)
armorLeather = Armor('Leather Armor','light',11)
armorStuddedLeather = Armor('Studded Leather Armor','light',13)

armorHide = Armor('Hide Armor','medium',12)
armorChainShirt = Armor('Chain Shirt','medium',13)
armorScaleMail = Armor('Scale Mail','medium',14)
armorBreastplate = Armor('Breasplate','medium',14)
armorHalfPlate = Armor('Half Plate','medium',15)

armorRingMail = Armor('Ring Mail','heavy',14)
armorChainMail = Armor('Chain Mail','heavy',16)
armorSplintMail = Armor('Splint Mail','heavy',17)
armorPlateMail = Armor('Plate Mail','heavy',18)

armorList = [
    armorPadded,
    armorLeather,
    armorStuddedLeather,
    armorHide,
    armorChainShirt,
    armorScaleMail,
    armorBreastplate,
    armorHalfPlate,
    armorRingMail,
    armorChainMail,
    armorSplintMail,
    armorPlateMail
]