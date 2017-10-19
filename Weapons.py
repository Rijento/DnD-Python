from Items import *
class Weapon(object):
    def __init__(self,name,Type,Range,damage,properties):
        self.name = name
        self.Type = Type
        self.Range = Range
        self.damage = damage
        self.properties = properties
    def getName(self):
        return self.name
    def getWeaponType(self):
        return self.Type
    def getWeaponRange(self):
        return self.Range
    def getWeaponDamage(self):
        return self.damage
    def getWeaponProperties(self):
        return self.properties
    def __eq__(self, other):
        if (type(self) != type(other)):
            return False;
        if (self.name == other.name):
            return True;
        return False;

club = Weapon('Club','Bludgeoning','5 ft.','1d4','Light')
dagger = Weapon('Dagger','Piercing','5 ft.','1d4','Finesse, Light, Thrown (range 20/60)')
greatclub = Weapon('Greatclub','Bludgeoning','5 ft.','1d8','Two-handed')
handaxe = Weapon('Handaxe','Slashing','5 ft.','1d6','Light, Thrown (range 20/60)')
javelin = Weapon('Javelin','Piercing','5 ft.','1d6','Thrown (range 30/120)')
lightHammer = Weapon('Light Hammer','Bludgeoning','5 ft.','1d4','Light, Thrown (range 20/60)')
mace = Weapon('Mace','Bludgeoning','5 ft.','1d6','')
quarterstaff = Weapon('Quarterstaff','Bludgeoning','5 ft.','1d6','Versatile (1d8)')
sickle = Weapon('Sickle','Slashing','5 ft.','1d4','Light')
spear = Weapon('Spear','Piercing','5 ft.','1d6','Thrown (range 20/60), Versatile (1d8)')
unarmedstrike = Weapon('Unarmed Strike', 'Bludgeoning','5 ft.','1','')
crossbowlight = Weapon('Light Crossbow','Piercing','80/320 ft.','1d8','Ammunition, Loading, Two-Handed')
dart = Weapon('Dart','Piercing','20/60 ft.','1d4','Finesse, Thrown')
shortbow = Weapon('Shortbow','Piercing','80/320 ft.','1d6','Ammunition, Two-Handed')
sling = Weapon('Sling','Bludgeoning','30/120 ft.','1d6','Ammunition')
battleaxe = Weapon('Battleaxe','Slashing','5 ft.','1d8','Versatile (1d10)')
flail = Weapon('Flail','Bludgeoning','5 ft.','1d8','')
glaive = Weapon('Glaive','Slashing','10 ft.','1d10','Heavy, Two-Handed')
greataxe = Weapon('Greataxe','Slashing','5 ft.','1d12','Heavy, Two-Handed')
greatsword = Weapon('Greatsword','Slashing','5 ft.','2d6','Heavy, Two-Handed')
halberd = Weapon('Halberd','Slashing','10 ft.','1d10','Heavy, Two-Handed')
lance = Weapon('Lance','Piercing','10 ft.','1d12',
    'You have disadvantage when attacking a target within 5 feet of you.\
    Two-Handed unless on horseback.')
longsword = Weapon('Longsword','Slashing','5 ft.','1d8','Versatile (1d10)')
maul = Weapon('Maul','Bludgeoning','5 ft.','2d6','Heavy, Two-Handed')
morningstar = Weapon('Morningstar','Piercing','5 ft.','1d8','')
pike = Weapon('Pike','Piercing','10 ft.','1d10','Heavy, Two-Handed')
rapier = Weapon('Rapier','Piercing','5 ft.','1d8','Finesse')
scimitar = Weapon('Scimitar','Slashing','5 ft.','1d6','Finesse, Light')
shortsword = Weapon('Shortsword','Piercing','5 ft.','1d6','Finesse, Light')
trident = Weapon('Trident','Piercing','5 ft.','1d6','Thrown (range 20/60), Versatile (1d8)')
warpick = Weapon('War pick','Piercing','5 ft.','1d8','')
warhammer = Weapon('Warhammer','Bludgeoning','5 ft.','1d8','Versatile (1d10)')
whip = Weapon('Whip','Slashing','10 ft.','1d4','Finesse')
blowgun = Weapon('Blowgun','Piercing','25/100 ft.','1','Ammunition, Loading')
crossbowhand = Weapon('Hand Crossbow','Piercing','30/120 ft.','1d6','Ammunition, Light, Loading')
crossbowheavy = Weapon('Heavy Crossbow','Piercing','100/400 ft.','1d10','Ammunition, Heavy, Loading, Two-Handed')
longbow = Weapon('Longbow','Piercing','150/600 ft.','1d8','Ammunition, Heavy, Two-Handed')
net = Weapon('Net','N/A','5/15 ft.','0',
    'Thrown, A Large or smaller creature hit by a net is\
    restrained until it is freed. A net has no effect on\
    creatures that are formless. A creature can use its\
    action to make a DC 10 Strength check, freeing itself\
    or another creature within its reach on a success.\
    Dealing 5 slashing damage to the net (AC 10) also\
    frees the creature without harming it, ending the\
    effect and destroying the net. When you use an action,\
    bonus action, or reaction to attack with a net, you\
    can make only one attack regardless of the number of\
    attacks you can normally make.')

weaponList = [club,
    dagger,
    greatclub,
    handaxe,
    javelin,
    lightHammer,
    mace,
    quarterstaff,
    sickle,
    spear,
    unarmedstrike,
    crossbowlight,
    dart,
    shortbow,
    sling,
    battleaxe,
    flail,
    glaive,
    greataxe,
    greatsword,
    halberd,
    lance,
    longsword,
    maul,
    morningstar,
    pike,
    rapier,
    scimitar,
    shortsword,
    trident,
    warpick,
    warhammer,
    whip,
    blowgun,
    crossbowhand,
    crossbowheavy,
    longbow,
    net]