class Item(object):
    def __init__(self, name, bWeight):
        self.name = name
        self.bWeight = bWeight
        self.quantity = 1

    def getItemName(self):
        return self.name

    def getItemWeight(self):
        return self.bWeight*self.quantity
    def setItemWeight(self, weight):
        self.bWeight = weight

    def setItemQuantity(self, num):
        self.quantity = num
    def getItemQuantity(self):
        return self.quantity

abacus = Item('Abacus',2)
acidVial = Item('Vial of Acid',1)
alchemistfire = Item('Flask of Alchemist\'s Fire',1)
arrow = Item('Arrows',0.05)
blowgunAmmo = Item('Blowgun Needles',0.02)
cbowBolts = Item('Crossbow Bolts',0.075)
slingAmmo = Item('Sling Bullets',0.075)
antitoxinVial = Item('Vial of Antitoxin',0)
crystal = Item('Arcane Crystal',1)
arcaneOrb = Item('Arcane Orb',3)
arcaneRod = Item('Arcane Rod',2)
arcaneStaff = Item('Arcane Staff',4)
arcaneWand = Item('Arcane wand',1)
backpack = Item('Backpack',5)
ballBearings = Item('Bag of Ball Bearings',2)
barrel = Item('Barrel',70)
basket = Item('Basket',2)
bedroll = Item('Bedroll',7)
bell = Item('Bell',0)
blanket = Item('Blanket',3)
blockTackle = Item('Block and Tackle',5)
book = Item('Book',5)
glassBottle = Item('Glass Bottle',2)
bucket = Item('Bucket',2)
caltropsBag = Item('Bag of Caltrops',2)
candle = Item('Candle',0)
boltCase = Item('Crossbow Bolt Case',1)
mapscrollCase = Item('Map/Scroll Case',1)
chain = Item('1 foot of Chain',1)
chalk = Item('Piece of Chalk',0)
chest = Item('Chest',25)
climberKit = Item('Climber\'s Kit',12)
copper = Item('Bar of Copper',1)
clothesCommon = Item('Common Clothes',3)
clothesCostume = Item('Costume Clothes',4)
clothesFine = Item('Fine Clothes',6)
clothesTraveler = Item('Traveler\'s Clothes',4)
componentPouch = Item('Component Pouch',2)
crowbar = Item('Crowbar',5)
druidicMistletoe = Item('Druidic Mistletoe Sprig',0)
druidicTotem = Item('Druidic Totem',0)
druidicStaff = Item('Druidic Wooden Staff',4)
druidicWand = Item('Druidic Yew Wand',1)
fishingTackle = Item('Fishing Tackle',4)
flaskTankard = Item('Flask/Tankard',1)
gold = Item('Bar of Gold',1)
grapplingHook = Item('Grappling Hook',4)
hammer = Item('Hammer',3)
sledgehammer = Item('Sledgehammer',10)
healerKit = Item('Healer\'s kit',3)
holyAmulet = Item('Holy Amulet',1)
holyEmblem = Item('Holy Emblem',0)
holyReliquary = Item('Holy Reliquary',2)
holyWater = Item('Flask of Holy Water',1)
hourglass = Item('Hourglass',1)
huntingTrap = Item('Hunting trap',25)
incense = Item('Block of Incense',0)
inkBottle = Item('Bottle of Ink',0)
inkPen = Item('Ink Pen',0)
iron = Item('Bar of Iron',1)
jugPitcher = Item('Jug/Pitcher',4)
ladder = Item('10-foot Ladder',25)
lamp = Item('Lamp',1)
lanternBullseye = Item('Bullseye Lantern',2)
lanternHooded = Item('Hooded Lantern',2)
lock = Item('Lock',1)
magnifyingGlass = Item('Magnifying Glass',0)
manacles = Item('Manacles',6)
messKit = Item('Mess Kit',1)
mirrorSteel = Item('Steel Mirror',0.5)
oilFlask = Item('Flask of Oil',1)
paperSheet = Item('Sheet of Paper',0)
parchmentSheet = Item('Sheet of Parchment',0)
perfumeVial = Item('Vial of Perfume',0)
minersPick = Item('Miner\'s pick',10)
piton = Item('Piton',0.25)
platinum = Item('Bar of Platinum',1)
poisonVial = Item('Vial of Poison',0)
pole10foot = Item('10-foot Pole',7)
potIron = Item('Iron Pot',10)
healingPotion = Item('Potion of Healing',0.5)
pouch = Item('Pouch',1)
quiver = Item('Quiver',1)
ramPortable = Item('Portable Ram',35)
rations = Item('Rations',2)
robes = Item('Robes',4)
ropeHemp = Item('1 foot of Hempen Rope',0.2)
ropeSilk = Item('1 foot of Silk Rope',0.1)
sack = Item('Sack',0.5)
merchantScale = Item('Merchant\'s Scale',3)
sealingWax = Item('Sealing Wax',0)
shovel = Item('Shovel',5)
silver = Item('Bar of Silver',1)
signalWhistle = Item('Signal Whistle',0)
signetRing = Item('Signet Ring',0)
soap = Item('Soap',0)
spellbook = Item('Spellbook',3)
ironSpikes = Item('Iron Spikes',0.5)
spyglass = Item('Spyglass',1)
tent2person = Item('Two-Person Tent',20)
tinderbox = Item('Tinderbox',1)
torch = Item('Torch',1)
vialEmpty = Item('Empty Vial',0)
waterskin = Item('Waterskin',5)
whetstone = Item('Whetstone',1)
suppliesAlchemist = Item('Alchemist\'s Supplies',8)
suppliesBrewer = Item('Brewer\'s Supplies',9)
suppliesCalligrapher = Item('Calligrapher\'s Supplies',5)
toolsCarpenter = Item('Carpenter\'s Tools',6)
toolsCartographer = Item('Cartographer\'s Tools',6)
toolsCobbler = Item('Cobbler\'s Tools',5)
toolsCook = Item('Cook\'s Tools',8)
utensilsCook = Item('Cook\'s Utensils',5)
toolsGlassblower = Item('Glassblower\'s Tools',5)
toolsJeweler = Item('Jeweler\'s Tools',4)
toolsLeatherworker = Item('Leatherworker\'s Tools',5)
toolsMason = Item('Mason\'s Tools',8)
suppliesPainter = Item('Painter\'s Supplies',5)
toolsPotter = Item('Potter\'s Tools',3)
toolsSmith = Item('Smith\'s Tools',8)
toolsTinker = Item('Tinker\'s Tools',10)
toolsWeaver = Item('Weaver\'s Tools',5)
toolsWoodcarver = Item('Woodcarver\'s Tools',5)
disguiseKit = Item('Disguise Kit',3)
forgeryKit = Item('Forgery Kit',5)
diceSet = Item('Dice Set',0)
dragonchessSet = Item('Dragonchess Set',0.5)
playingCardSet = Item('Playing Card Set',0)
threeDragonAnteSet = Item('Three-Dragon Ante Set',0)
herbalismKit = Item('Herbalism Kit',3)
bagpipes = Item('Bagpipes',6)
drum = Item('Drum',3)
dulcimer = Item('Dulcimer',10)
flute = Item('Flute',1)
lute = Item('Lute',2)
lyre = Item('Lyre',2)
horn = Item('Horn',2)
panFlute = Item('Pan Flute',2)
shawm = Item('Shawm',1)
viol = Item('Viol',1)
toolsNavigator = Item('Navigator\'s Tools',2)
poisonerKit = Item('Poisoner\'s Kit',2)
toolsThieves = Item('Thieves\' Tools',1)

## ARMORS ##
armorPadded = Item('Padded Armor',8)
armorLeather = Item('Leather Armor',10)
armorStuddedLeather = Item('Studded Leather Armor',13)
armorHide = Item('Hide Armor',12)
armorChainShirt = Item('Chain Shirt',20)
armorScaleMail = Item('Scale Mail',45)
armorBreastplate = Item('Breasplate',20)
armorHalfPlate = Item('Half Plate',40)
armorRingMail = Item('Ring Mail',40)
armorChainMail = Item('Chain Mail',55)
armorSplintMail = Item('Splint Mail',60)
armorPlateMail = Item('Plate Mail',65)
shield = Item('Shield',6)

armorItems = [
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

## WEAPONS ##

ammoList = [
    arrow,
    blowgunAmmo,
    cbowBolts,
    slingAmmo
]

generalToolList = [
    blockTackle,
    bedroll,
    climberKit,
    crowbar,
    fishingTackle,
    grapplingHook,
    hammer,
    sledgehammer,
    healerKit,
    huntingTrap,
    ladder,
    lamp,
    lanternBullseye,
    lanternHooded,
    lock,
    magnifyingGlass,
    messKit,
    minersPick,
    piton,
    pole10foot,
    ramPortable,
    merchantScale,
    shovel,
    spyglass,
    tinderbox,
    tent2person,
    torch,
    whetstone
]

otherList = [
    abacus,
    acidVial,
    alchemistfire,
    antitoxinVial,
    ballBearings,
    bedroll,
    bell,
    blanket,
    book,
    caltropsBag,
    candle,
    chain,
    chalk,
    copper,
    gold,
    hourglass,
    incense,
    inkBottle,
    inkPen,
    iron,
    manacles,
    mirrorSteel,
    paperSheet,
    parchmentSheet,
    perfumeVial,
    platinum,
    poisonVial,
    healingPotion,
    rations,
    ropeHemp,
    ropeSilk,
    sealingWax,
    signalWhistle,
    signetRing,
    soap,
    spellbook,
    ironSpikes
]

containerList = [
    backpack,
    barrel,
    basket,
    glassBottle,
    bucket,
    boltCase,
    mapscrollCase,
    chest,
    componentPouch,
    flaskTankard,
    pouch,
    quiver,
    sack,
    vialEmpty,
    waterskin
]

specialToolList = [
    suppliesAlchemist,
    suppliesBrewer,
    suppliesCalligrapher,
    toolsCarpenter,
    toolsCartographer,
    toolsCobbler,
    toolsCook,
    utensilsCook,
    toolsGlassblower,
    toolsJeweler,
    toolsLeatherworker,
    toolsMason,
    suppliesPainter,
    toolsPotter,
    toolsSmith,
    toolsTinker,
    toolsWeaver,
    toolsWoodcarver,
    disguiseKit,
    forgeryKit,
    herbalismKit,
    toolsNavigator,
    poisonerKit,
    toolsThieves
]

arcabeFociList = [
    crystal,
    arcaneOrb,
    arcaneRod,
    arcaneStaff,
    arcaneWand
]

druidicFociList = [
    druidicMistletoe,
    druidicTotem,
    druidicStaff,
    druidicWand
]

holySymbolList = [
    holyAmulet,
    holyEmblem,
    holyReliquary
]

clothesList = [
    clothesCommon,
    clothesCostume,
    clothesFine,
    clothesTraveler,
    robes
]

gamesList = [
    diceSet,
    dragonchessSet,
    playingCardSet,
    threeDragonAnteSet
]

instrumentList = [
    bagpipes,
    drum,
    dulcimer,
    flute,
    lute,
    lyre,
    horn,
    panFlute,
    shawm,
    viol
]

itemList = [
    abacus,
    acidVial,
    alchemistfire,
    arrow,
    blowgunAmmo,
    cbowBolts,
    slingAmmo,
    antitoxinVial,
    crystal,
    arcaneOrb,
    arcaneRod,
    arcaneStaff,
    arcaneWand,
    backpack,
    ballBearings,
    barrel,
    basket,
    bedroll,
    bell,
    blanket,
    blockTackle,
    book,
    glassBottle,
    bucket,
    caltropsBag,
    candle,
    boltCase,
    mapscrollCase,
    chain,
    chalk,
    chest,
    climberKit,
    copper,
    clothesCommon,
    clothesCostume,
    clothesFine,
    clothesTraveler,
    componentPouch,
    crowbar,
    druidicMistletoe,
    druidicTotem,
    druidicStaff,
    druidicWand,
    fishingTackle,
    flaskTankard,
    gold,
    grapplingHook,
    hammer,
    sledgehammer,
    healerKit,
    holyAmulet,
    holyEmblem,
    holyReliquary,
    holyWater,
    hourglass,
    huntingTrap,
    incense,
    inkBottle,
    inkPen,
    iron,
    jugPitcher,
    ladder,
    lamp,
    lanternBullseye,
    lanternHooded,
    lock,
    magnifyingGlass,
    manacles,
    messKit,
    mirrorSteel,
    oilFlask,
    paperSheet,
    parchmentSheet,
    perfumeVial,
    minersPick,
    piton,
    platinum,
    poisonVial,
    pole10foot,
    potIron,
    healingPotion,
    pouch,
    quiver,
    ramPortable,
    rations,
    robes,
    ropeHemp,
    ropeSilk,
    sack,
    merchantScale,
    sealingWax,
    shovel,
    silver,
    signalWhistle,
    signetRing,
    soap,
    spellbook,
    ironSpikes,
    spyglass,
    tent2person,
    tinderbox,
    torch,
    vialEmpty,
    waterskin,
    whetstone,
    suppliesAlchemist,
    suppliesBrewer,
    suppliesCalligrapher,
    toolsCarpenter,
    toolsCartographer,
    toolsCobbler,
    toolsCook,
    utensilsCook,
    toolsGlassblower,
    toolsJeweler,
    toolsLeatherworker,
    toolsMason,
    suppliesPainter,
    toolsPotter,
    toolsSmith,
    toolsTinker,
    toolsWeaver,
    toolsWoodcarver,
    disguiseKit,
    forgeryKit,
    diceSet,
    dragonchessSet,
    playingCardSet,
    threeDragonAnteSet,
    herbalismKit,
    bagpipes,
    drum,
    dulcimer,
    flute,
    lute,
    lyre,
    horn,
    panFlute,
    shawm,
    viol,
    toolsNavigator,
    poisonerKit,
    toolsThieves
]