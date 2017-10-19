class Feature(object):
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    def getFeatureName(self):
        return self.name
    def getFeatureDesc(self):
        return self.desc
    def __hash__(self):
        return hash(self.name)
    def __eq__(self,other):
        return self.name == other.name

#Race &subrace Features
#Dwarf features
darkvision = Feature('Darkvision','You can see in dim light within 60 feet of you as\nif it were bright light, and in darkness as if it\nwere dim light. You can\'t discern color in darkness,\nonly shades of gray.')
dwarvenResilience = Feature('Dwarven Resiliance','You have advantage on saving throws against poison,\nand you have resistance against poison damage.')
dwarvenCombatTraining = Feature('Dwarven Combat Training','You have proficiency with the battleaxe, handaxe,\nthrowing hammer, and warhammer.')
stonecunning = Feature('Stonecunning','Whenever you make an Intelligence check related to\nthe origin of stonework, you are considered\nproficient in the History skill and add double your\nproficiency bonus to the check, instead of your\nnormal proficiency bonus.')
#Hill Dwarf
dwarvenToughness = Feature('Dwarven Toughness','Your hit point maximum increases by 1, and it\nincreases by 1 every time you gain a level.')
#Mountain Dwarf
dwarvenArmorTraining = Feature('Dwarven Armor Training','You have proficiency with light and medium armor.')

#elf features
#darkvision
keenSenses = Feature('Keen Senses','You have proficiency in the Perception Skill.')
feyAncestry = Feature('Fey Ancestry','You have advantage on saving throws against being\ncharmed, and magic can\'t put you to sleep.')
trance = Feature('Trance','Instead of sleeping for 8 hours, you only need to\nmeditate for 4.')
#High Elf
cantripElf = Feature('Cantrip','You know one cantrip of your choice from the wizard\nspell list. Intelligence is your spellcasting ability for it.')
elfWeaponTraining = Feature('Elf Weapon Training','You have proficiency with the longsword, shortsword,\nshortbow, and longbow.')
#wood elf
#elf weapon training
maskOfTheWild = Feature('Mask of the Wild','You can attempt to hide even when you are only\nlightly obscured by foliage, heavy rain, falling\nsnow, mist, and other natural phenomena.')
#dark elf
superiorDarkvision = Feature('Superior Darkvision','Your darkvision has a radius of 120 feet.')
drowMagic = Feature('Drow Magic','You know the dancing lights cantrip. When you reach\n3rd level, you can cast the faerie fire spell once\nper day. When you reach 5th level, you can also\ncast the darkness spell once per day. Charisma is\nyour spellcasting ability for these spells.')
sunlightSensitivity = Feature('Sunlight Sensitivity','You have disadvantage on attack rolls and on\nperception checks that rely on sight when you, the\ntarget of your attack, or whatever you are trying\nto perceive is in direct sunlight.')
drowWeaponTraining = Feature('Drow Weapon Training','You are proficient with rapiers, shortswords, and\nhand crossbows.')

#halfling features
lucky = Feature('Lucky','When you roll a 1 on an attack roll, ability check,\nor saving throw, you can reroll the die and must\nuse the new roll.')
brave = Feature('Brave','You have an advantage on saving throws against\nbeing frightened.')
halflingNimbleness = Feature('Halfling Nimbleness','You can move through the space of any creature that\nis of a size larger than yours.')
#lightfoot
naturallyStealthy = Feature('Naturally Stealthy','You can attempt to hide even when you are obscured\nonly by a creature that is at least one size larger\nthan you.')
#stout
stoutResilience = Feature('Stout Resilience','You have advantage on saving throws against poison,\nand you have resistance against poison damage.')

#Human Features
#NONE

#Dragonborn Features
#Black Dragonborn
draconicAncestryBlack = Feature('Draconic Ancestry','The blood of a Black Dragon runs through your veins.')
breathWeaponBlack = Feature('Breath Weapon','You can use you action to exhale a destructive splash\nof acid in a 5 by 30 ft. line before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceBlackDrag = Feature('Damage Resistance','You have resistance against acid damage.')
#Blue Dragonborn
draconicAncestryBlue = Feature('Draconic Ancestry','The blood of a Blue Dragon runs through your veins.')
breathWeaponBlue = Feature('Breath Weapon','You can use you action to exhale a destructive bolt\nof ligntning in a 5 by 30 ft. line before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceBlueDrag = Feature('Damage Resistance','You have resistance against lightning damage.')
#Brass Dragonborn
draconicAncestryBrass = Feature('Draconic Ancestry','The blood of a Brass Dragon runs through your veins.')
breathWeaponBrass = Feature('Breath Weapon','You can use you action to exhale a destructive blast\nof fire in a 5 by 30 ft. line before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceBrassDrag = Feature('Damage Resistance','You have resistance against fire damage.')
#Bronze Dragonborn
draconicAncestryBronze = Feature('Draconic Ancestry','The blood of a Bronze Dragon runs through your veins.')
breathWeaponBronze = Feature('Breath Weapon','You can use you action to exhale a destructive bolt\nof ligntning in a 5 by 30 ft. line before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceBronzeDrag = Feature('Damage Resistance','You have resistance against lightning damage.')
#Copper Dragonborn
draconicAncestryCopper = Feature('Draconic Ancestry','The blood of a Copper Dragon runs through your veins.')
breathWeaponCopper = Feature('Breath Weapon','You can use you action to exhale a destructive splash\nof acid in a 5 by 30 ft. line before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceCopperDrag = Feature('Damage Resistance','You have resistance against acid damage.')
#Gold Dragonborn
draconicAncestryGold = Feature('Draconic Ancestry','The blood of a Gold Dragon runs through your veins.')
breathWeaponGold = Feature('Breath Weapon','You can use you action to exhale a destructive blast\nof fire in a 15 ft. cone before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceGoldDrag = Feature('Damage Resistance','You have resistance against fire damage.')
#Green Dragonborn
draconicAncestryGreen = Feature('Draconic Ancestry','The blood of a Green Dragon runs through your veins.')
breathWeaponGreen = Feature('Breath Weapon','You can use you action to exhale a destructive cloud\nof poison in a 15 ft. cone before you.\nA creature takes 2d6 damage on a failed (Con)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceGreenDrag = Feature('Damage Resistance','You have resistance against poison damage.')
#Red Dragonborn
draconicAncestryRed = Feature('Draconic Ancestry','The blood of a Red Dragon runs through your veins.')
breathWeaponRed = Feature('Breath Weapon','You can use you action to exhale a destructive blast\nof fire in a 15 ft. cone before you.\nA creature takes 2d6 damage on a failed (Dex)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceRedDrag = Feature('Damage Resistance','You have resistance against fire damage.')
#Silver Dragonborn
draconicAncestrySilver = Feature('Draconic Ancestry','The blood of a Silver Dragon runs through your veins.')
breathWeaponSilver = Feature('Breath Weapon','You can use you action to exhale a destructive wave\nof frigid air in a 15 ft. cone before you.\nA creature takes 2d6 damage on a failed (Con)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceSilverDrag = Feature('Damage Resistance','You have resistance against cold damage.')
#White Dragonborn
draconicAncestryWhite = Feature('Draconic Ancestry','The blood of a White Dragon runs through your veins.')
breathWeaponWhite = Feature('Breath Weapon','You can use you action to exhale a destructive wave\nof frigid air in a 15 ft. cone before you.\nA creature takes 2d6 damage on a failed (Con)\nsaving throw, and half as much damage on a\nsuccessful one.\nDC = 8 + your Con modifier + your proficiency bonus.\nYou must complete a long or short rest before another\nbreath attack.')
damageResistanceWhiteDrag = Feature('Damage Resistance','You have resistance against cold damage.')

#Gnome features
#Darkvision
gnomeCunning = Feature('Gnome Cunning','You have advantage on all Intelligence, Wisdom,\nand Charisma saving throws against magic.')
#forest gnome
naturalIllusionist = Feature('Natural Illusionist','You know the minor illusion cantrip. Intelligence\nis your spellcasting ability for it.')
speakWithSmallBeasts = Feature('Speak with Small Beasts','Through sounds and gestures, you can communicate\nsimple ideas with small or smaller beasts.')
#rock gnome
artificersLore = Feature('Artificer\'s Lore','Whenever you make a History check related to magic\nitems, alchemical objects, or technological devices,\nyou can add twice your proficiency bonus, instead\nof any proficiency bonus you normally apply.')
tinkerGnome = Feature('Tinker','You have proficiency with tinker\'s tools.\nUsing those tools, you can spend 1 hour and 10 gp\nworth of materials to construct a tiny clockwork\ndevice (AC 5, 1 hp). The device ceases to function\nafter 24 hours unless you spend 1 repairing it.\nYou can also use your action to dismantle it; at\nthat time you can reclaim the materials used to\ncreate it. You can have up to three such devices\nat active at a time.\nWhen you create a device, choose one of the\nfollowing options:\nClockwork Toy:\n\tWhen placed on the ground, the toy moves 5 feet\n\tacross the ground on each of your turns in a random\n\tdirection. It makes noises appropriate to the\n\tcreature it resembles.\nFire Starter:\n\tThe device produces a miniature flame, which you\n\tcan use to light a candle, torch, or campfire.\n\tUsing the device requires your action.\nMusic Box:\n\tPlays music when opened, ceasing when either\n\treaching the song\'s end or when it is closed.')

#half-elf features
#darkvision
#feyAncestry

#Half orc features
#darkvision
menacing = Feature('Menacing','You gain proficiency in the Intimidation skill.')
relentlessEndurance = Feature('Relentless Endurance','When you are reduced to 0 hit points but not killed\noutright, you can drop to 1 hit point instead. You\ncan\'t use this feature again until you finish a\nlong rest.')
savageAttacks = Feature('Savage Attacks','When you score a critical hit with a melee weapon\nattack, you can roll one of the weapon\'s damage\ndice one additional time and add it to the extra\ndamage of the critical hit.')

#Tiefling features
#darkvision
hellishResistance = Feature('Hellish Resistance','You have resistance to fire damage.')
infernalLegacy = Feature('Infernal Legacy','You know the thaumaturgy cantrip. Once you reach\n3rd level, you can cast the hellish rebuke spell\nonce per day as a 2nd-level spell. Once you reach\n5th level, you can also cast the darkness spell\nonce per day. Charisma is your spellcasting ability\nfor these spells.')


#Class Features
#barbarian
rageL1 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +2 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 2 times, you must finish a long rest\n\
before you can rage again.')
unarmoredDefenseBarbarian = Feature('Unarmored Defense','While you are not wearing any armor, your Armor Class\n\
equals 10 + your Dexterity modifier + your Constitution\n\
modifier. You can use a shield and still gain this benefit.')
#Level2
recklessAttack = Feature('Relentless Attack',
'You can throw aside all concern for defense to attack\n\
with fierce desperation. When you make your first\n\
attack on your turn, you can decide to attack recklessly.\n\
Doing so gives you advantage on melee weapon attack\n\
rolls using Strength during this turn, but attack rolls\n\
against you have advantage until your next turn.\n')
dangerSense = Feature('Danger Sense',
'You gain an uncanny sense of when things nearby aren\'t\n\
as they should be, giving you an edge when you dodge\n\
away from danger.\n\
    You have advantage on Dexterity saving throws\n\
against effects that you can see, such as traps and spells.\n\
To gain this benefit, you can\'t be blinded, deafened, or\n\
incapacitated.')
#level3
rageL2 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +2 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 3 times, you must finish a long rest\n\
before you can rage again.')

primalPathBerserker = Feature('Path of the Berserker',
'For some barbarians, rage is a means to an end—that\n\
end being violence. The Path of the B erserker is a path\n\
of untrammeled fury, slick with blood. As you enter\n\
the berserker\'s rage, you thrill in the chaos of battle,\n\
heedless of your own health or well-being.')
frenzy = Feature('Frenzy',
'You can go into a frenzy when you rage. If you do so, for\n\
the duration of your rage you can make a single melee\n\
weapon attack as a bonus action on each of your turns\n\
after this one. When your rage ends, you suffer one level\n\
of exhaustion.')

primalPathTotem = Feature('Path of the Totem Warrior',
'The Path of the Totem Warrior is a spiritual journey, as\n\
the barbarian accepts a spirit animal as guide, protector,\n\
and inspiration. In battle, your totem spirit fills you\n\
with supernatural might, adding magical fuel to your\n\
barbarian rage.')
spiritSeeker = Feature('Spirit Seeker',
'Yours is a path that seeks attunement with the natural\n\
world, giving you a kinship with beasts. When you adopt this\n\
path, you gain the ability to cast the beast sense and speak\n\
with animals spells, but only as rituals.')
totemSpiritBear = Feature('Totem Spirit: Bear',
'You must make or acquire a physical totem object—an\n\
amulet or similar adornment—that in corporates fur,\n\
claws, teeth, or bones of a Bear.\n\
Once you have a totem, you gain the following effect:\n\
    While raging, you have resistance to all damage\n\
    except psychic damage. The spirit of the bear makes\n\
    you tough enough to stand up to any punishment.')
totemSpiritEagle = Feature('Totem Spirit: Eagle',
'You must make or acquire a physical totem object—an\n\
amulet or similar adornment—that in corporates feathers,\n\
talons, or bones of an Eagle.\n\
Once you have a totem, you gain the following effect:\n\
    While you\'re raging and aren\'t wearing heavy\n\
    armor, other creatures have disadvantage on\n\
    opportunity attack rolls against you, and you\n\
    can use the Dash action as a bonus action on your\n\
    turn. The spirit of the eagle makes you into a\n\
    predator who can weave through the fray with ease.')
totemSpiritWolf = Feature('Totem Spirit: Wolf',
'You must make or acquire a physical totem object—an\n\
amulet or similar adornment—that in corporates fur,\n\
claws, teeth, or bones of a Wolf.\n\
Once you have a totem, you gain the following effect:\n\
    While you\'re raging, your friends have advantage\n\
    on melee attack rolls against any creature within\n\
    5 feet of you that is hostile to you. The spirit of\n\
    the wolf makes you a leader of hunters.')
#level5
extraAttack = Feature('Extra Attack',
'You can attack twice, instead of once whenever you take\n\
the Attack action on your turn.')
fastMovementBarb = Feature('Fast Movement',
'Your speed increases by 10 feet while you aren\'t\n\
wearing heavy armor.')
#level6
rageL3 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +2 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 4 times, you must finish a long rest\n\
before you can rage again.')

mindlessRage = Feature('Mindless Rage',
'You can\'t be charmed or frightened while raging. If you\n\
are charmed or frightened when you enter your rage, the\n\
effect is suspended for the duration of the rage.')

aspectBeastBear = Feature('Aspect of the Beast: Bear',
'You gain the might of a bear. Your carrying capacity\n\
(including maximum load and maximum lift) is doubled,\n\
and you have advantage on Strength checks made to push,\n\
pull, lift, or break objects.')
aspectBeastEagle = Feature('Aspect of the Beast: Eagle',
'You gain the eyesight of an eagle. You can see up to\n\
1 mile away with no difficulty, able to discern even\n\
fine details as though looking at something no more\n\
than 100 feet away from you. Additionally, dim light\n\
doesn\'t impose disadvantage on your Perception checks.')
aspectBeastWolf = Feature('Aspect of the Beast: Wolf',
'You gain the hunting sensibilities of a wolf. You can\n\
track other creatures while traveling at a fast pace, and\n\
you can move stealthily while traveling at a normal pace.')
#level7
feralInstinct = Feature('Feral Instinct',
'Your instincts are so h oned that you have advantage on\n\
initiative rolls.\n\
Additionally, if you are surprised at the beginning of\n\
combat and aren\'t incapacitated, you can act normally\n\
on your first turn, but only if you enter your rage before\n\
doing anything else on that turn.')
#level9
brutalCriticalL1 = Feature('Brutal Critical',
'You can roll one additional weapon damage die when\n\
determining the extra damage for a critical hit with\n\
a melee attack.')
rageL4 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +3 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 4 times, you must finish a long rest\n\
before you can rage again.')
#level10
intimidatingPresence = Feature('Intimidating Presence',
'You can use your action to frighten someone with your\n\
menacing presence. When you do so, choose one creature\n\
that you can see within 30 feet of you. If the creature\n\
can see or hear you, it must succeed on a Wisdom saving\n\
throw (DC equal to 8 + your proficiency bonus + your\n\
Charisma modifier) or be frightened of you until the\n\
end of your next turn. On subsequent turns, you can use\n\
your action to extend the duration of this effect on\n\
the frightened creature until the end of your next turn.\n\
This effect ends if the creature ends its turn out of\n\
line of sight or more than 60 feet away from you.\n\
    If the creature succeeds on its saving throw, you\n\
can\'t use this feature on that creature again for 24 hours.')

spiritWalker = Feature('Spirit Walker',
'You can cast the commune with nature spell, but only\n\
as a ritual. When you do so, a spiritual version of\n\
one of the animals you chose for Totem Spirit or\n\
Aspect of the Beast appears to you to convey the\n\
information you seek.')
#level11
relentlessRage = Feature('Relentless Rage',
'Your rage can keep you fighting despite grievous wounds.\n\
If you drop to 0 hit points while you\'re raging and\n\
don\'t die outright, you can make a DC 10 Constitution\n\
saving throw. If you succeed, you drop to 1 hit point\n\
instead.\n\
    Each time you use this feature after the first, the DC\n\
increases by 5. When you finish a short or long rest, the\n\
DC resets to 10.')
#level12
rageL5 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +3 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 5 times, you must finish a long rest\n\
before you can rage again.')
#level13
brutalCriticalL2 = Feature('Brutal Critical',
'You can roll two additional weapon damage die when\n\
determining the extra damage for a critical hit with\n\
a melee attack.')
#level14
retaliation = Feature('Retaliation',
'When you take damage from a creature that is within\n\
5 feet of you. you can use your reaction to make a\n\
melee weap on attack against that creature.')

totemicAttunementBear = Feature('Totemic Attunement: Bear',
'You gain the might of a bear. Your carrying capacity\n\
(including maximum load and maximum lift) is doubled,\n\
and you have advantage on Strength checks made to push,\n\
pull, lift, or break objects.')

totemicAttunementEagle = Feature('Totemic Attunement: Eagle',
'You gain the eyesight of an eagle. You can see up to\n\
1 mile away with no difficulty, able to discern\n\
even fine details as though looking at something no\n\
more than 100 feet away from you. Additionally, dim\n\
light doesn\'t impose disadvantage on your Wisdom\n\
(Perception) checks.')

totemicAttunementWolf = Feature('Totemic Attunement: Wolf',
'You gain the hunting sensibilities of a wolf. You can\n\
track other creatures while traveling at a fast pace,\n\
and you can move stealthily while traveling at a normal\n\
pace.')

#level15
persistantRage = Feature('Persistant Rage',
'Your rage is so fierce that it ends early only\n\
if you fall unconscious or if you choose to end it.')


#level16
rageL6 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +4 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 5 times, you must finish a long rest\n\
before you can rage again.')

#level17
brutalCriticalL3 = Feature('Brutal Critical',
'You can roll three additional weapon damage die when\n\
determining the extra damage for a critical hit with\n\
a melee attack.')
rageL7 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +4 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
Once you have raged 6 times, you must finish a long rest\n\
before you can rage again.')

#level18
indomitableMight = Feature('Indomitable Might',
'If your total for a Strength check is less than\n\
your Strength score, you can use that score in\n\
place of the total.')

#level20
primalChampion = Feature('Primal Champion',
'You embody the power of the wilds. Your Strength and\n\
Constitution scores increase by 4. Your maximum for\n\
those scores is now 24.')
rageL8 = Feature('Rage','In battle, you fight with prim al ferocity. O n your turn,\n\
you can enter a rage as a bonus action.\n\
While raging, you gain the following benefits if you\n\
aren\'t wearing heavy armor:\n\
• You have advantage on Strength checks and Strength\n\
  saving throws.\n\
• When you make a melee weapon attack using\n\
  Strength, you gain a +4 bonus to the damage roll.\n\
• You have resistance to bludgeoning, piercing, and\n\
  slashing damage.\n\
If you are able to cast spells, you can\'t cast them or\n\
concentrate on them while raging.\n\
Your rage lasts for 1 minute. It ends early if you are\n\
knocked unconscious or if your turn ends and you\n\
haven’t attacked a hostile creature since your last turn\n\
or taken damage since then. You can also end your rage\n\
on your turn as abonus action.\n\
You have no limit to the number of rages you can enter.')





#Bard Features 
spellcastingBardL1 = Feature('Spellcasting',
'You know two cantrips of your choice from the bard spell list.\n\
    You know 4 1st level spells of your choice from the bard\n\
spell list and possess 2 1st level spell slots. To cast one of\n\
these spells, you must expend a slot of the spell\'s level\n\
or higher. You regain all expended spell slots when you\n\
finish a long rest.')
bardicInspirationL1 = Feature('Bardic Inspiration',
'You can inspire others through stirring words or music.\n\
To do so, you use a bonus action on your turn to choose\n\
one creature other than yourself within 60 feet of you\n\
who can hear you. That creature gains one Bardic\n\
Inspiration die, a d6.\n\
Once within the next 10 minutes, the creature can roll\n\
the die and add the number rolled to one ability check,\n\
attack roll, or saving throw it makes. The creature can\n\
wait until after it rolls the d20 before deciding to use the\n\
Bardic Inspiration die, but must decide before the DM\n\
says whether the roll succeeds or fails. Once the Bardic\n\
Inspiration die is rolled, it is lost. A creature can have\n\
only one Bardic Inspiration die at a time. You can use this\n\
feature a number of times equal to your Charisma modifier\n\
(a minimum of once). You regain any expended uses when you\n\
finish a long rest.')

#level 2
spellcastingBardL2 = Feature('Spellcasting',
'You know two cantrips of your choice from the bard spell list.\n\
    You know 5 spells of your choice from the bard spell\n\
list and possess 3 1st level spell slots. To cast one of\n\
these spells, you must expend a slot of the spell\'s level\n\
or higher. You regain all expended spell slots when you\n\
finish a long rest.')
jackOfAllTrades = Feature('Jack of All Trades',
'You can add half your proficiency bonus, rounded down, to\n\
any ability check you make that doesn\'t already include\n\
your proficiency bonus.')
songOfRestL1 = Feature('Song of Rest',
'You can use soothing music or oration to help revitalize\n\
your wounded allies during a short rest. If you or\n\
any friendly creatures who can hear your performance\n\
regain hit points at the end of the short rest, each of\n\
those creatures regains an extra 1d6 hit points.')

#level 3
spellcastingBardL3 = Feature('Spellcasting',
'You know two cantrips of your choice from the bard spell list.\n\
    You know 6 spells of your choice from the bard spell\n\
list and possess 4 1st level spell slots and 2 2nd level\n\
spell slots. To cast one of these spells, you must expend\n\
a slot of the spell\'s level or higher. You regain all expended\n\
spell slots when you finish a long rest.')
edpertiseL1 = Feature('Expertise',
'Choose two of your skill proficiencies. Your proficiency\n\
bonus is doubled for any ability check you make that uses\n\
either of the chosen proficiencies.')

collegeLore = Feature('College of Lore',
'Bards of the College of Lore know something about\n\
most things, collecting bits of knowledge from sources\n\
as diverse as scholarly tomes and peasant tales.\n\
Whether singing folk ballads in taverns or elaborate\n\
compositions in royal courts, these bards use their gifts\n\
to hold audiences spellbound. When the applause dies\n\
down, the audience members might find them selves\n\
questioning everything they held to be true, from their\n\
faith in the priesthood of the local temple to their\n\
loyalty to the king.')
bonusProficienciesLore = Feature('Bonus Proficiencies',
'When you join the College of Lore, you gain\n\
proficiency with three skills of your choice.')
cuttingWords = Feature('Cutting Words',
'You learn how to use your wit to distract, confuse,\n\
and otherwise sap the confidence and competence of others.\n\
When a creature that you can see within 60 feet\n\
of you makes an attack roll, an ability check, or a damage\n\
roll, you can use your reaction to expend one of your\n\
uses of Bardic Inspiration, rolling a Bardic Inspiration\n\
die and subtracting the number rolled from the\n\
creature\'s roll. You can choose to use this feature after\n\
the creature makes its roll, but before the DM determines\n\
whether the attack roll or ability check succeeds or fails,\n\
or before the creature deals its damage. The creature\n\
is immune if it can\'t hear you or if it\'s immune to\n\
being charmed.')

collegeValor = Feature('College of Valor',
'Bards of the College of Valor are daring skalds whose\n\
tales keep alive the memory of the great heroes of the\n\
past, and thereby inspire a new generation of heroes.\n\
These bards gather in mead halls or around great\n\
bonfires to sing the deeds of the mighty, both past\n\
and present. They travel the land to witness great\n\
events firsthand and to ensure that the memory of\n\
those events doesn\'t pass from the world. With their\n\
songs, they inspire others to reach the same heights of\n\
accomplishment as the heroes of old.')
bonusProficienciesValor = Feature('Bonus Proficiencies',
'When you join the College of Valor, you gain proficiency\n\
with medium armor, shields, and martial weapons.')
combatInspiration = Feature('Combat Inspiration',
'You learn to inspire others in battle. A creature that has\n\
a Bardic Inspiration die from you can roll that die\n\
and add the number rolled to a weapon damage roll it just\n\
made. Alternatively, when an attack roll is made against\n\
the creature, it can use its reaction to roll the Bardic\n\
Inspiration die and add the number rolled to its AC\n\
against that attack, after seeing the roll but before\n\
knowing whether it hits or misses.')

#level 4
spellcastingBardL4 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 7 spells of your choice from the bard spell\n\
list and possess 4 1st level spell slots and 3 2nd level\n\
spell slots. To cast one of these spells, you must expend\n\
a slot of the spell\'s level or higher. You regain all expended\n\
spell slots when you finish a long rest.')

#level 5
spellcastingBardL5 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 8 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, and 2 3rd level\n\
spell slots. To cast one of these spells, you must expend\n\
a slot of the spell\'s level or higher. You regain all expended\n\
spell slots when you finish a long rest.')
bardicInspirationL2 = Feature('Bardic Inspiration',
'You can inspire others through stirring words or music.\n\
To do so, you use a bonus action on your turn to choose\n\
one creature other than yourself within 60 feet of you\n\
who can hear you. That creature gains one Bardic\n\
Inspiration die, a d8.\n\
Once within the next 10 minutes, the creature can roll\n\
the die and add the number rolled to one ability check,\n\
attack roll, or saving throw it makes. The creature can\n\
wait until after it rolls the d20 before deciding to use the\n\
Bardic Inspiration die, but must decide before the DM\n\
says whether the roll succeeds or fails. Once the Bardic\n\
Inspiration die is rolled, it is lost. A creature can have\n\
only one Bardic Inspiration die at a time. You can use this\n\
feature a number of times equal to your Charisma modifier\n\
(a minimum of once). You regain any expended uses when you\n\
finish a long rest.')
fontOfInspiration = Feature('Font of Inspiration',
'You regain all of your expended uses of Bardic Inspiration\n\
when you finish a short or long rest.')

#level 6
spellcastingBardL6 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 9 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, and 3 3rd level\n\
spell slots. To cast one of these spells, you must expend\n\
a slot of the spell\'s level or higher. You regain all expended\n\
spell slots when you finish a long rest.')
countercharm = Feature('Countercharm',
'You gain the ability to use musical notes or words of power\n\
to disrupt mind-influencing effects. As an action, you\n\
can start a performance that lasts until the end of your\n\
next turn. During that time, you and any friendly\n\
creatures within 30 feet of you have advantage on saving throws\n\
against being frightened or charmed. A creature must\n\
be able to hear you to gain this benefit. The performance\n\
ends early if you are incapacitated or silenced or if\n\
you voluntarily end it (no action required).')

additionalMagicalSecrets = Feature('Additional Magical Secrets',
'You learn two spells of your choice from any class. A spell\n\
you choose must be of a level you can cast, or a cantrip.\n\
The chosen spells count as bard spells for you but don\'t\n\
count against the number of bard spells you know.')

#extra attack

#level 7
spellcastingBardL7 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 10 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level, and\n\
1 4th level spell slots. To cast one of these spells, you must\n\
expend a slot of the spell\'s level or higher. You regain all\n\
expended spell slots when you finish a long rest.')

#level 8
spellcastingBardL8 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 11 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level, and\n\
2 4th level spell slots. To cast one of these spells, you must\n\
expend a slot of the spell\'s level or higher. You regain all\n\
expended spell slots when you finish a long rest.')

#level 9
spellcastingBardL9 = Feature('Spellcasting',
'You know three cantrips of your choice from the bard spell list.\n\
    You know 12 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, and 1 5th level spell slots. To cast one of\n\
these spells, you must expend a slot of the spell\'s level or\n\
higher. You regain all expended spell slots when you finish a\n\
long rest.')

songOfRestL2 = Feature('Song of Rest',
'You can use soothing music or oration to help revitalize\n\
your wounded allies during a short rest. If you or\n\
any friendly creatures who can hear your performance\n\
regain hit points at the end of the short rest, each of\n\
those creatures regains an extra 1d8 hit points.')

#level 10
spellcastingBardL10 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 14 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, and 2 5th level spell slots. To cast one of\n\
these spells, you must expend a slot of the spell\'s level or\n\
higher. You regain all expended spell slots when you finish a\n\
long rest.')
bardicInspirationL3 = Feature('Bardic Inspiration',
'You can inspire others through stirring words or music.\n\
To do so, you use a bonus action on your turn to choose\n\
one creature other than yourself within 60 feet of you\n\
who can hear you. That creature gains one Bardic\n\
Inspiration die, a d10.\n\
Once within the next 10 minutes, the creature can roll\n\
the die and add the number rolled to one ability check,\n\
attack roll, or saving throw it makes. The creature can\n\
wait until after it rolls the d20 before deciding to use the\n\
Bardic Inspiration die, but must decide before the DM\n\
says whether the roll succeeds or fails. Once the Bardic\n\
Inspiration die is rolled, it is lost. A creature can have\n\
only one Bardic Inspiration die at a time. You can use this\n\
feature a number of times equal to your Charisma modifier\n\
(a minimum of once). You regain any expended uses when you\n\
finish a long rest.')
edpertiseL2 = Feature('Expertise',
'Choose four of your skill proficiencies. Your proficiency\n\
bonus is doubled for any ability check you make that uses\n\
either of the chosen proficiencies.')
magicalSecretsL1 = Feature('Magical Secrets',
'You have plundered magical knowledge from a wide\n\
spectrum of disciplines. Choose two spells from any class,\n\
including this one. A spell you choose must be of a\n\
level you can cast, or a cantrip.\n\
    The chosen spells count as bard spells for you and are\n\
included in the number in the Spells Known column of\n\
the Bard table.')

#level 11
spellcastingBardL11 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 15 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, and 1 6th level spell slots. To cast one\n\
of these spells, you must expend a slot of the spell\'s level or\n\
higher. You regain all expended spell slots when you finish a\n\
long rest.')

#level 12
spellcastingBardL12 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 15 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, and 1 6th level spell slots. To cast one\n\
of these spells, you must expend a slot of the spell\'s level or\n\
higher. You regain all expended spell slots when you finish a\n\
long rest.')

#level 13
spellcastingBardL13 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 16 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, 1 6th level, and 1 7th level spell slots.\n\
To cast one of these spells, you must expend a slot of the spell\'s\n\
level or higher. You regain all expended spell slots when you finish\n\
a long rest.')
songOfRestL3 = Feature('Song of Rest',
'You can use soothing music or oration to help revitalize\n\
your wounded allies during a short rest. If you or\n\
any friendly creatures who can hear your performance\n\
regain hit points at the end of the short rest, each of\n\
those creatures regains an extra 1d10 hit points.')

#level 14
spellcastingBardL14 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 18 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, 1 6th level, and 1 7th level spell slots.\n\
To cast one of these spells, you must expend a slot of the spell\'s\n\
level or higher. You regain all expended spell slots when you finish\n\
a long rest.')
magicalSecretsL2 = Feature('Magical Secrets',
'You have plundered magical knowledge from a wide\n\
spectrum of disciplines. Choose four spells from any class,\n\
including this one. A spell you choose must be of a\n\
level you can cast, or a cantrip.\n\
    The chosen spells count as bard spells for you and are\n\
included in the number in the Spells Known column of\n\
the Bard table.')

peerlessSkill = Feature('Peerless Skill',
'When you make an ability check, you can expend one use of\n\
Bardic Inspiration. Roll a Bardic Inspiration die\n\
and add the number rolled to your ability check. You\n\
can choose to do so after you roil the die for the ability\n\
check, but before the DM tells you whether you succeed or fail.')

battleMagic = Feature('Battle Magic',
'You have mastered the art of weaving spellcasting and\n\
weapon use into a single harmonious act. When you use\n\
your action to cast a bard spell, you can make one\n\
weapon attack as a bonus action.')

#level 15
spellcastingBardL15 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 19 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, 1 6th level, 1 7th level, and\n\
1 8th level spell slots. To cast one of these spells, you must\n\
expend a slot of the spell\'s level or higher. You regain all\n\
expended spell slots when you finish a long rest.')
bardicInspirationL4 = Feature('Bardic Inspiration',
'You can inspire others through stirring words or music.\n\
To do so, you use a bonus action on your turn to choose\n\
one creature other than yourself within 60 feet of you\n\
who can hear you. That creature gains one Bardic\n\
Inspiration die, a d12.\n\
Once within the next 10 minutes, the creature can roll\n\
the die and add the number rolled to one ability check,\n\
attack roll, or saving throw it makes. The creature can\n\
wait until after it rolls the d20 before deciding to use the\n\
Bardic Inspiration die, but must decide before the DM\n\
says whether the roll succeeds or fails. Once the Bardic\n\
Inspiration die is rolled, it is lost. A creature can have\n\
only one Bardic Inspiration die at a time. You can use this\n\
feature a number of times equal to your Charisma modifier\n\
(a minimum of once). You regain any expended uses when you\n\
finish a long rest.')

#level 16
spellcastingBardL16 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 19 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, 1 6th level, 1 7th level, and\n\
1 8th level spell slots. To cast one of these spells, you must\n\
expend a slot of the spell\'s level or higher. You regain all\n\
expended spell slots when you finish a long rest.')

#level 17
spellcastingBardL17 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 20 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 2 5th level, 1 6th level, 1 7th level, 1 8th\n\
level, and 1 9th level spell slots. To cast one of these spells,\n\
you must expend a slot of the spell\'s level or higher. You regain\n\
all expended spell slots when you finish a long rest.')
songOfRestL3 = Feature('Song of Rest',
'You can use soothing music or oration to help revitalize\n\
your wounded allies during a short rest. If you or\n\
any friendly creatures who can hear your performance\n\
regain hit points at the end of the short rest, each of\n\
those creatures regains an extra 1d12 hit points.')

#level 18
spellcastingBardL18 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 22 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 3 5th level, 1 6th level, 1 7th level, 1 8th\n\
level, and 1 9th level spell slots. To cast one of these spells,\n\
you must expend a slot of the spell\'s level or higher. You regain\n\
all expended spell slots when you finish a long rest.')
magicalSecretsL3 = Feature('Magical Secrets',
'You have plundered magical knowledge from a wide\n\
spectrum of disciplines. Choose six spells from any class,\n\
including this one. A spell you choose must be of a\n\
level you can cast, or a cantrip.\n\
    The chosen spells count as bard spells for you and are\n\
included in the number in the Spells Known column of\n\
the Bard table.')

#level 19
spellcastingBardL19 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 22 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 3 5th level, 2 6th level, 1 7th level, 1 8th\n\
level, and 1 9th level spell slots. To cast one of these spells,\n\
you must expend a slot of the spell\'s level or higher. You regain\n\
all expended spell slots when you finish a long rest.')

#level 20
spellcastingBardL20 = Feature('Spellcasting',
'You know four cantrips of your choice from the bard spell list.\n\
    You know 22 spells of your choice from the bard spell\n\
list and possess 4 1st level, 3 2nd level, 3 3rd level,\n\
3 4th level, 3 5th level, 2 6th level, 2 7th level, 1 8th\n\
level, and 1 9th level spell slots. To cast one of these spells,\n\
you must expend a slot of the spell\'s level or higher. You regain\n\
all expended spell slots when you finish a long rest.')
superiorInspiration = Feature('Superior Inspiration',
'When you roll initiative and have no uses of Bardic\n\
Inspiration left, you regain one use.')




#Cleric
spellcastingClericL1 = Feature('Spellcasting',
'You know three cantrips of your choice from the cleric spell list.\n\
You possess 2 1st level spell slots.\n\
    You prepare the list of cleric spells that are available\n\
for you to cast, choosing from the cleric spell list. When\n\
you do so, choose a number of cleric spells equal to\n\
your Wisdom modifier + your cleric level (minimum of\n\
one spell). The spells must be of a level for which you\n\
have spell slots.\n\
    You can change your list of prepared spells when you\n\
finish a long rest. Preparing a new list of cleric spells\n\
requires time spent in prayer and meditation: at least 1\n\
minute per spell level for each spell on your list.')

divineDominKnowledge = Feature('Domain of Knowledge',
'The gods of knowledge—including Oghma, Boccob,\n\
Gilean, Aureon, and Thoth—value learning and\n\
understanding above all. Followers of these gods study\n\
esoteric lore, collect old tomes, delve into the secret\n\
places of the earth, and learn all they can.')
knowledgeDomainSpellsL1 = Feature('Knowledge Domain Spells',
'You know the spells command and identify.')
blessingsOfKnowledge = Feature('Blessings of Knowledge',
'You learn two languages of your choice. You also become\n\
proficient in your choice of two of the following skills:\n\
Arcana, History, Nature, or Religion.\n\
    Your proficiency bonus is doubled for any ability check\n\
you make that uses either of those skills.')

divineDominLife = Feature('Domain of Life',
'The Life domain focuses on the vibrant positive\n\
energy—one of the fundamental forces of the universe—\n\
that sustains all life. The gods of life promote vitality\n\
and health through healing the sick and wounded,\n\
caring for those in need, and driving away the forces of\n\
death and undeath.')
lifeDomainSpellsL1 = Feature('Life Domain Spells',
'You know the spells bless and cure wounds.')
bonusProficiencyLifeDomain = Feature('Bonus Proficiency',
'You gain proficiency with heavy armor')
disciplineOfLife = Feature('Discipline of Life',
'Your healing spells are more effective. Whenever you use a\n\
spell of 1st level or higher to restore hit points to a\n\
creature, the creature regains additional hit points equal\n\
to 2 + the spell\'s level.')

divineDominLight = Feature('Domain of Life',
'Gods of light—including Helm, Lathander, Pholtus,\n\
Branchala, the Silver Flame, Belenus, Apollo, and\n\
Re-Horakhty—promote the ideals of rebirth and\n\
renewal, truth, vigilance, and beauty, often using the\n\
symbol of the sun. Clerics of a god of light are \n\
enlightened souls infused with radiance and the\n\
power of their gods\' discerning vision, charged\n\
with chasing away lies and burning away darkness.')
lightDomainSpellsL1 = Feature('Light Domain Spells',
'You know the spells burning hands and faerie fire.')
bonusCantripLightDomain = Feature('Bonus Cantrip',
'You gain the light cantrip if you don\'t already know it.')
wardingFlare = Feature('Warding Flare',
'You can interpose divine light between yourself and an\n\
attacking enemy. When you are attacked by a creature within\n\
30 feet of you that you can see, you can use your\n\
reaction to impose disadvantage on the attack roll, causing\n\
light to flare in front of the attacker before it hits or\n\
misses. An attacker that can\'t be blinded is immune to this\n\
feature.\n\
    You can use this feature a number of times equal to\n\
your Wisdom modifier (a minimum of once). You regain\n\
all expended uses when you finish a long rest.')

divineDominNature = Feature('Domain of Nature',
'Many gods of nature have clerics as well, champions who\n\
take a more active role in advancing their particular\n\
interests. These clerics might hunt the evil monstrosities\n\
that despoil the woodlands, bless the harvest of the\n\
faithful, or wither the crops of those who anger their gods.')
natureDomainSpellsL1 = Feature('Nature Domain Spells',
'You know the spells animal friendship and speak with animals.')
bonusProficiencyNatureDomain = Feature('Bonus Proficiency',
'You gain proficiency with heavy armor.')
acolyteOfNature = Feature('Acolyte of Nature',
'You learn one druid cantrip of your choice. You also gain\n\
proficiency in one of the following skills of your choice:\n\
Animal Handling, Nature, or Survival.')

divineDominTempest = Feature('Domain of Tempest',
'Gods whose portfolios include the Tempest domain—\n\
including Talos, Umberlee, Kord, Zeboim, the\n\
Devourer, Zeus, and Thor—govern storms, sea, and\n\
sky. Tempest gods send their clerics to inspire fear\n\
in the common folk, either to keep those folk on the\n\
path of righteousness or to encourage them to offer\n\
sacrifices of propitiation to ward off divine wrath.')
tempestDomainSpells = Feature('Tempest Domain Spells',
'You know the spells fog cloud and thunderwave.')
bonusProficienciesTempestDomain = Feature('Bonus Proficiencies',
'You gain proficiency with martial weapons and heavy armor.')

divineDominTrickery = None

divineDominWar = None








#Druid
druidic = Feature('Druidic','You know Druidic, the secret language of druids. You\n\
can speak the language and use it to leave hidden\n\
messages. You and others who know this language\n\
automatically spot such a message. Others spot the\n\
message\'s presence with a successful DC 15 Wisdom\n\
(Perception) check but can\'t decipher it without magic.')
druidicSpellcastingL1 = Feature('Spellcasting',
'You know two cantrips of your choice from the druid spell list.\n\
    You have two 1st level spell slots. To cast one of\n\
these druid spells, you must expend a slot of the spell’s\n\
level or higher. You regain all expended spell slots when\n\
you finish a long rest.\n\
    You prepare the list of druid spells that are available\n\
for you to cast, choosing from the druid spell list. When\n\
you do so, choose a number of druid spells equal to\n\
your Wisdom modifier + your druid level (minimum of\n\
one spell). The spells must be of a level for which you\n\
have spell slots.\n\
    You can also change your list of prepared spells when\n\
you finish a long rest. Preparing a new list of druid\n\
spells requires time spent in prayer and meditation: at\n\
least 1 minute per spell level for each spell on your list.')

#fighter
secondWind = Feature('Second Wind','You have a limited well of stamina that you can draw on\n\
to protect yourself from harm. On your turn, you can use\n\
a bonus action to regain hit points equal to 1d10 + your\n\
fighter level.\n\
Once you use this feature, you must finish a short or\n\
long rest before you can use it again.')
fightingStyle = Feature('Fighting Style','Under Construction. Please come back later!')

#monk
unarmoredDefenseMonk = Feature('Unarmored Defense','Beginning at 1st level, while you are wearing no armor\n\
and not wielding a shield, your AC equals 10 + your\n\
Dexterity modifier + your Wisdom modifier.')
martialArtsMonkL1 = Feature('Martial Arts','As a monk, your practice of martial arts gives you\n\
mastery of combat styles that use unarmed strikes and\n\
monk weapons, which are shortswords and any simple\n\
melee weapons that don\'t have the two-handed or\n\
heavy property.\n\
You gain the following benefits while you are unarmed\n\
or wielding only monk weapons and you aren\'t wearing\n\
armor or wielding a shield:\n\
• You can use Dexterity instead of Strength for the\n\
  attack and damage rolls of your unarmed strikes and\n\
  monk weapons.\n\
• You can roll a d4 in place of the normal damage\n\
  of your unarmed strike or monk weapon.\n\
• When you use the Attack action with an unarmed\n\
  strike or a monk weapon on your turn, you can make\n\
  one unarmed strike as a bonus action. For example, if\n\
  you take the Attack action and attack with a quarter-\n\
  staff, you can also make an unarmed strike as a bonus\n\
  action, assuming you haven\'t already taken a bonus\n\
  action this turn.')

#paladin
divineSensePaladin = Feature('Divine Sense','The presence of stron gevil registers on your senses like\n\
a noxious odor, and powerful good rings like heavenly\n\
music in your ears. As an action, you can open your\n\
awareness to detect such forces. Until the end of your\n\
next turn, you know the location of any celestial, fiend,\n\
or undead within 60 feet of you that is not behind total\n\
cover. You know the type (celestial, fiend, or undead) of\n\
any being whose presence you sense, but not its identity\n\
(the vampire Count Strahd von Zarovich, for instance).\n\
Within the same radius, you also detect the presence\n\
of any place or object that has been consecrated or\n\
desecrated, as with the hallow spell.\n\
You can use this feature a number of times equal to\n\
1 + your Charisma modifier. When you finish a long rest,\n\
you regain all expended uses.')
PaladinLayOnHandsL1 = Feature('Lay on Hands','Your blessed touch can heal wounds. You have a pool\n\
of healing power that replenishes when you take a long\n\
rest. With that pool, you can restore a total number of\n\
hit points equal to your paladin level x 5.\n\
    As an action, you can touch a creature and draw\n\
power from the pool to restore a number of hit points\n\
to that creature, up to the maximum amount remaining\n\
in your pool.\n\
    Alternatively, you can expend 5 hit points from your\n\
pool of healing to cure the target of one disease or\n\
neutralize one poison affecting it. You can cure multiple\n\
diseases and neutralize multiple poisons with a single\n\
use of Lay on Hands, expending hit points separately\n\
for each one.\n\
    This feature has no effect on undead and constructs.')

#Ranger
favoredEnemyRangerL1 = Feature('Favored Enemy','You have significant experience\n\
studying, tracking, hunting, and even talking to a certain\n\
type of enemy.\n\
    Choose a type of favored enemy: aberrations,\n\
beasts, celestials, constructs, dragons, elementals, fey,\n\
fiends, giants, monstrosities, oozes, plants, or undead.\n\
Alternatively, you can select two races of humanoid\n\
(such as gnolls and orcs) as favored enemies.\n\
You have advantage on Wisdom (Survival) checks to\n\
track your favored enemies, as well as on Intelligence\n\
checks to recall inform ation about them.\n\
When you gain this feature, you also learn one\n\
language of your choice that is spoken by your favored\n\
enemies, if they speak one at all.')
naturalExplorerRangerL1 = Feature('Natural Explorer','You are particularly familiar with one type of natural\n\
environment and are adept at traveling and surviving in\n\
such regions. Choose one type of favored terrain: arctic,\n\
coast, desert, forest, grassland, mountain, swamp,\n\
or the Underdark. When you make an Intelligence or\n\
Wisdom check related to your favored terrain, your\n\
proficiency bonus is doubled if you are using a skill that\n\
you\'re proficient in.\n\
    While traveling for an hour or more in your favored\n\
terrain, you gain the following benefits:\n\
• Difficult terrain doesn\'t slow your group\'s travel.\n\
• Your group can\'t become lost except by magical\n\
  means.\n\
• Even when you are engaged in another activity while\n\
  traveling (such as foraging, navigating, or tracking),\n\
  you remain alert to danger.\n\
• If you are traveling alone, you can move stealthily at\n\
  a normal pace.\n\
• When you forage, you find twice as much food as you\n\
  normally would.\n\
• While tracking other creatures, you also learn their\n\
  exact number, their sizes, and how long ago they\n\
  passed through the area.')

#rogue
expertiseRogueL1 = Feature('Expertise','At 1st level, choose two of your skill proficiencies, or\n\
one of your skill proficiencies and your proficiency with\n\
thieves\' tools. Your proficiency bonus is doubled for any\n\
ability check you make that uses either of the chosen\n\
proficiencies.')
sneakAttackRogueL1 = Feature('Sneak Attack','Beginning at 1st level, you know how to strike subtly\n\
and exploit a foe\'s distraction. Once per turn, you can\n\
deal an extra 1d6 dam age to one creature you hit with\n\
an attack if you have advantage on the attack roll. The\n\
attack must use a finesse or a ranged weapon .\n\
    You don\'t need advantage on the attack roll if another\n\
enemy of the target is within 5 feet of it, that enemy\n\
isn\'t incapacitated, and you don\'t have disadvantage on\n\
the attack roll.')
thievesCant = Feature('Thieves\' Cant','During your rogue training you learned thieves\' cant, a\n\
secret mix of dialect, jargon, and code that allows you to\n\
hide messa ges in seemingly normal conversation. Only\n\
another creature that knows thieves\' cant understands\n\
such messages. It takes four times longer to convey such\n\
a message than it does to speak the same idea plainly.\n\
    In addition, you understand a set of secret signs and\n\
symbols used to convey short, simple messa ges, such\n\
as whether an area is dangerous or the territory of a\n\
thieves\' guild, whether loot is nearby, or whether the\n\
people in an area are easy marks or will provide a safe\n\
house for thieves on the run.')

#sorcerer
spellcastingSorcererL1 = Feature('Spellcasting','At 1st level, you know four cantrips of your choice from\n\
the sorcerer spell list.\n\
    You have two 1st level spell slots. To cast one of your\n\
spells, you must expend a slot of the spell\'s level or \n\
higher. You regain all expended spell slots when you\n\
finish a long rest.\n\
    You know two 1st-level spells of your choice from the\n\
sorcerer spell list.')
sorcerousOrigin = Feature('Sorcerous Origin','Under Construction. Please come back later!')

#Warlock
otherworldlyPatron = Feature('Otherworldly Patron','Under Construction. Please come back later!')
pactMagicWarlockL1 = Feature('Pact Magic','You know two cantrips of your choice from the warlock\n\
spell list.\n\
    You have one 1st level spell slot. To cast one of your\n\
warlock spells of 1st level or higher, you must expend a\n\
spell slot. You regain all expended spell slots when you\n\
finish a short or long rest.\n\
    At 1st level, you know two 1st-level spells of your choice\n\
from the warlock spell list.')

#Wizard
spellcastingWizardL1 = Feature('Spellcasting','At 1st level, you know three cantrips of your choice\n\
from the wizard spell list.\n\
    At 1st level, you have a spellbook containing six 1st-level\n\
wizard spells of your choice.\n\
    At 1st level, you have two 1st level spell slots. To cast one of\n\
these spells, you must expend a slot of the spell’s level\n\
or higher. You regain all expended spell slots when you\n\
finish a long rest.\n\
    You prepare the list of wizard spells that are available\n\
for you to cast. To do so. choose a number of wizard\n\
spells from your spellbook equal to your Intelligence\n\
modifier + your wizard level (minimum of one spell). The\n\
spells must be of a level for which you have spell slots.\n\
    You can change your list of prepared spells when\n\
you finish a long rest. Preparing a new list of wizard\n\
spells requires time spent studying your spellbook and\n\
memorizing the incantations and gestures you must\n\
make to cast the spell: at least 1 minute per spell level\n\
for each spell on your list.')
arcaneRecovery = Feature('Arcane Recovery','You have learned to regain some of your magical energy\n\
by studying your spellbook. Once per day when you\n\
finish a short rest, you can choose expended spell slots\n\
to recover. The spell slots can have a combined level that\n\
is equal to or less than half your wizard level (rounded\n\
up), and none of the slots can be 6th level or higher.')

#Backgrounds
#Acolyte
shelterOfTheFaithful = Feature('Shelter of the Faithful','As an acolyte, you command the respect of those who\n\
share your faith, and you can perform the religious\n\
ceremonies of your deity. You and your adventuring\n\
companion s can expect to receive free healing and\n\
care at a temple, shrine, or other established presence\n\
of your faith, though you must provide any material\n\
com ponents needed for spells. Those who share\n\
your religion will support you (but only you) at a\n\
modest lifestyle.')

#Charlatan
falseIdentity = Feature('False Identity','You have created a second identity that includes\n\
documentation, established acquaintances, and\n\
disguises that allow you to assume that persona.\n\
Additionally, you can forge documents including official\n\
papers and personal letters, as long as you have seen an\n\
example of the kind of document or the handwriting you\n\
are trying to copy.')

#Criminal
criminalContact = Feature('Criminal Contact','You have a reliable and trustworthy contact who acts as\n\
your liaison to a network of other criminals. You know\n\
how to get messages to and from your contact, even\n\
over great distances; specifically, you know the local\n\
messengers, corrupt caravan masters, and seedy sailors\n\
who can deliver messages for you.')

#Entertainer
byPopularDemand = Feature('By Popular Demand','You can always find a place to perform, usually in an\n\
inn or tavern but possibly with a circus, at a theater, or\n\
even in a noble\'s court. At such a place, you receive free\n\
lodging and food of a modest or comfortable standard\n\
(depending on the quality of the establishment), as\n\
long as you perform each night. In addition, your\n\
performance makes you something of a local figure.\n\
When strangers recognize you in a town w here you have\n\
performed, they typically take a liking to you.')

#Folk Hero
rusticHospitality = Feature('Rustic Hospitality','Since you come from the ranks of the common folk,\n\
you fit in among them with ease. You can find a place\n\
to hide, rest, or recuperate among other commoners,\n\
unless you have shown yourself to be a danger to\n\
them. They will shield you from the law or anyone\n\
else searching for you, though they will not risk\n\
their lives for you.')

#Guild Artisan
guildMembership = Feature('Guild Membership','As an established and respected member of a guild, you\n\
can rely on certain benefits that membership provides.\n\
Your fellow guild mem bers will provide you with\n\
lodging and food if necessary, and pay for your funeral\n\
if needed. In some cities and towns, a guildhall offers a\n\
central place to meet other members of your profession,\n\
which can be a good place to meet potential patrons,\n\
allies, or hirelings.\n\
    Guilds often wield tremendous political power. If\n\
you are accused of a crime, your guild will support you\n\
if a good case can be made for your innocenceor the\n\
crime is justifiable. You can also gain access to powerful\n\
political figures through the guild, if you are a member\n\
in good standing. Such connections might require the\n\
donation of money or magic items to the guild\'s coffers.\n\
    You must pay dues of 5 gp per month to the guild. If\n\
you miss payments, you must make up back dues to\n\
remain in the guild\'s good graces.')

#hermit
discovery = Feature('Discovery',
'The quiet seclusion of your extended hermitage gave you\n\
access to a unique and powerful discovery. The exact\n\
nature of this revelation depends on the nature of your\n\
seclusion. It might be a great truth about the cosmos,\n\
the deities, the powerful beings of the outer planes, or\n\
the forces of nature. It could be a site that no one else\n\
has ever seen. You might have uncovered a fact that has\n\
long been forgotten, or unearthed some relic of the past\n\
that could rewrite history. It might be information that\n\
would be damaging to the people who consigned you\n\
to exile, and hence the reason for your return to society.\n\
    Work with your DM to determine the details of your\n\
discovery and its impact on the campaign.')

#Noble
positionOfPrivilege = Feature('Position of Privilege',
'Thanks to your noble birth, people are inclined to\n\
think the best of you. You are welcome in high society,\n\
and people assume you have the right to be wherever\n\
you are. The common folk make every effort to\n\
accommodate you and avoid your displeasure, and other\n\
people of high birth treat you as a member of the same\n\
social sphere. You can secure an audience with a local\n\
noble if you need to.')

#outlander
wanderer = Feature('Wanderer',
'You have an excellent memory for maps and geography,\n\
and you can always recall the general layout of terrain,\n\
settlements, and other features around you. In addition,\n\
you can find food and fresh water for yourself and up to\n\
five other people each day, provided that the land offers\n\
berries, small game, water, and so forth.')

#Sage
researcher = Feature('Researcher',
'When you attempt to learn or recall a piece of lore, if you\n\
do not know that inform ation, you often know where and\n\
from whom you can obtain it. Usually, this information\n\
comes from a library, scriptorium, university, or a sage\n\
or other learned person or creature. Your DM might\n\
rule that the knowledge you seek is secreted away in an\n\
almost inaccessible place, or that it simply cannot be\n\
found. Unearthing the deepest secrets of the multiverse\n\
can require an adventure or even a whole campaign.')
''
#sailor
shipsPassage = Feature('Ship\'s Passage',
'When you need to, you can secure free passage on\n\
a sailing ship for yourself and your adventuring\n\
companions. You might sail on the ship you served on,\n\
or another ship you have good relations with (perhaps\n\
one captained by a former crewmate). Because you\'re\n\
calling in a favor, you can\'t be certain of a schedule or\n\
route that will meet your every need. Your Dungeon\n\
Master will determine how long it takes to get where\n\
you need to go. In return for your free passage, you\n\
and your companions are expected to assist the crew\n\
during the voyage.')

#soldier
militaryRank = Feature('Miliary Rank',
'You have a military rank from your career as a soldier.\n\
Soldiers loyal to your former military organization\n\
still recognize your authority and influence, and they\n\
defer to you if they are of a lower rank. You can invoke\n\
your rank to exert influence over other soldiers and\n\
requisition simple equipment or horses for temporary\n\
use. You can also usually gain access to friendly\n\
military encampments and fortresses where your\n\
rank is recognized.')

#Urchin
citySecrets = Feature('City Secrets',
'You know the secret patterns and flow to cities and can\n\
find passages through the urban sprawl that others would\n\
miss. When you are not in combat, you (and companions\n\
you lead) can travel between any two locations in the city\n\
twice as fast as your speed would normally allow.')