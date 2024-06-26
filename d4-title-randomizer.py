import tkinter as tk
from tkinter import ttk
import random

# Arrays for prefixes and suffixes
prefixes = [
"Accomplished",
"Agile",
"Alarming",
"Amber",
"Anguished",
"Anointed",
"Anxious",
"Apex",
"Apprentice",
"Ardent",
"Aromatic",
"Ashen",
"Avid",
"Barreling",
"Belligerent",
"Bellowing",
"Bewitching",
"Bejeweled",
"Bitter",
"Bloodsoaked",
"Bloody",
"Blue",
"Bold",
"Bossy",
"Brash",
"Brave",
"Brittle",
"Brutal",
"Bubbly",
"Cackling",
"Callous",
"Carrion",
"Charnel",
"Chilling",
"Clever",
"Cold-Blooded",
"Committed",
"Complete",
"Consummate",
"Cormond's",
"Covetous",
"Crafty,"
"Crimson",
"Crushing",
"Crystalline",
"Cunning",
"Cutting",
"Dark",
"Daunting",
"Dauntless",
"Dazzling",
"Deadly",
"Dedicated",
"Devoted",
"Devilish",
"Diligent",
"Dire",
"Dirty",
"Distilled",
"Distracted",
"Dogged",
"Drowned",
"Drunken",
"Dry",
"Eldritch",
"Elemental",
"Embattled",
"Enlightened",
"Equestrian",
"Equipped",
"Essential",
"Eventful",
"Exalted",
"Faithful",
"Fallen",
"Fanged",
"Ferocious",
"Fleet",
"Foolish",
"Formless",
"Foul",
"Fractured",
"Fragrant",
"Frightening",
"Frightful",
"Frost",
"Furious",
"Giant",
"Gilded",
"Glen",
"Grave",
"Grim",
"Hallowed",
"Hasty",
"Hellish",
"Hermetic",
"Holy",
"Honored",
"Horned",
"Horrifying",
"Howling",
"Hungry",
"Hunter's",
"Imbued",
"Impious",
"Insatiable",
"Intense",
"Iron",
"Journeyed",
"Laughing",
"Legendary",
"Lethal",
"Lilith’s",
"Liminal",
"Little",
"Local",
"Lonely",
"Lucky",
"Lurking",
"Mad",
"Malevolent",
"Malicious",
"Malignant",
"Marsh",
"Merciless",
"Meticulous",
"Mighty",
"Murderous",
"Murmuring",
"Natural",
"Necromancer",
"Necrotic",
"Nefarious",
"Nightmare",
"Nocturnal",
"Novice",
"Overwhelming",
"Pained",
"Pale",
"Pallid",
"Paragon",
"Peerless",
"Potential",
"Prepared",
"Profane",
"Pyro",
"Quick",
"Rabid",
"Ravenous",
"Rampaging",
"Rending",
"Renaissance",
"Resourceful",
"Righteous",
"Risen",
"Rotten",
"Ruinous",
"Rusted",
"Sacred",
"Sanguine",
"Salty",
"Sanctified",
"Scarred",
"Scowling",
"Seasoned",
"Serial",
"Sharp",
"Shadow",
"Shambling",
"Shattered",
"Shifty",
"Sightless",
"Silken",
"Silver",
"Slinking",
"Smiling",
"Stamping",
"Steadfast",
"Steely",
"Stone",
"Sweaty",
"Succubus",
"Tempered",
"Terrible",
"Terrifying",
"Tidal",
"Timeless",
"Titan",
"The",
"Thorough",
"Transcended",
"Traveled",
"Treasure",
"Tormented",
"Tortured",
"Twisted",
"Unbroken",
"Unfettered",
"Unflagging",
"Unholy",
"Unseen",
"Upstart",
"Vain",
"Vampiric",
"Vault",
"Vengeful",
"Venomous",
"Vicious",
"Victorious",
"Vile",
"Vitreous",
"Voltaic",
"Voracious",
"Whispering",
"Wicked",
"Wily",
"Winding",
"Withering",
"Worldly",
"Wrathful",
"Zir's"
]

suffixes = [
"Abomination",
"Acolyte",
"Adventurer",
"Alchemist",
"Ally",
"Apothecary",
"Apprentice",
"Aristocrat",
"Armorer",
"Armoury",
"Aspirant",
"Assailant",
"Assassin",
"Band",
"Bandit",
"Bane",
"Barbarian",
"Baron",
"Bear",
"Beast",
"Believer",
"Blackguard",
"Blade",
"Blessing",
"Boots",
"Bounty",
"Braggart",
"Breaker",
"Brewer",
"Brewmaster",
"Brigadier",
"Brigand",
"Brute",
"Butcher",
"Casualty",
"Catastrophe",
"Challenger",
"Champion",
"Changeling",
"Charmer",
"Chef",
"Chieftain",
"Chorus",
"Commander",
"Claw",
"Cleaver",
"Cohort",
"Collector",
"Combatant",
"Commoner",
"Comrade",
"Connoisseur",
"Conductor",
"Conjurer",
"Conquerer",
"Coordinator",
"Curse",
"Creature",
"Culprit",
"Cutthroat",
"Dancer",
"Deadeye",
"Deathspeaker",
"Delver",
"Desert",
"Destroyer",
"Desolation",
"Devil",
"Devotee",
"Drifter",
"Dominance",
"Doom",
"Dread",
"Dredger",
"Druid",
"Dungeoneer",
"Eater",
"Echo",
"Elder",
"Enchanter",
"Executioner",
"Exemplar",
"Exorcist",
"Explorer",
"Fear",
"Fiend",
"Firestarter",
"Florist",
"Foe",
"Fool",
"Fortune-Hunter",
"Friend",
"Fugitive",
"Gambler",
"Genius",
"Ghost",
"Glutton",
"Goat",
"Grandmaster",
"Guardian",
"Harbinger",
"Harvester",
"Heart",
"Hellraiser",
"Herbalist",
"Heretic",
"Hero",
"Hoarder",
"Horadrim",
"Horror",
"Hound",
"Hunter",
"Iconoclast",
"Immortal",
"Imp",
"Initiate",
"Jeweler",
"Jockey",
"Killer",
"Kindred",
"Knight",
"Legend",
"Legion",
"Looter",
"Lord",
"Lout",
"Maestro",
"Maniac",
"Marauder",
"Mariner",
"Master",
"Menace",
"Mercy",
"Mess",
"Mindcage",
"Miner",
"Monster,"
"Murderer",
"Mystery",
"Nemesis",
"Nightmare",
"Onslaught",
"Opportunist",
"Paragon",
"Perfumer",
"Phantom",
"Pirate",
"Power",
"Predator",
"Protector",
"Purifier",
"Pursuer",
"Rage",
"Ransacker",
"Rapture",
"Rat",
"Ravager",
"Reaper",
"Rogue",
"Ruin",
"Sacrifice",
"Sage",
"Salvager",
"Scavenger",
"Scourge",
"Scout",
"Seeker",
"Scoundrel",
"Shaman",
"Shepherd",
"Shield",
"Sinner",
"Skinner",
"Skull",
"Slayer",
"Smith",
"Sorcerer",
"Sovereign",
"Specter",
"Spellbinder",
"Spider",
"Spirit",
"Squire",
"Stalker",
"Stranger",
"Striker",
"Sunderer",
"Supplanter",
"Surveyor",
"Survivor",
"Team",
"Tempest",
"Terror",
"Thief",
"Tinker",
"Toppler",
"Tracker",
"Traveler",
"Trickster",
"Tyrant",
"Tycoon",
"Underdog",
"Undertaker",
"Vampire",
"Vandal",
"Vanquisher",
"Vapor",
"Venturer",
"Victor",
"Villain",
"Vitality",
"Voice",
"Voyager",
"Wanderer",
"Warrior",
"Wayfarer",
"Witch",
"Worm",
"Wraith",
"Wretch",
"Wyrmfiend",
"Zealot",
"Zenith"
]

# Function to pick a random prefix
def pick_prefix():
    prefix_var.set(random.choice(prefixes))

# Function to pick a random suffix
def pick_suffix():
    suffix_var.set(random.choice(suffixes))
    
#Function to pick both
def pick_both():
    pick_prefix()
    pick_suffix()

# Initialize the main window
root = tk.Tk()
root.title("D4 Title Randomizer")

# Character Name
tk.Label(root, text="Character Name:").grid(row=0, column=0, padx=10, pady=10)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

# Prefix
tk.Label(root, text="Prefix:").grid(row=1, column=0, padx=10, pady=10)
prefix_var = tk.StringVar()
tk.Entry(root, textvariable=prefix_var).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Pick Prefix", command=pick_prefix).grid(row=1, column=2, padx=10, pady=10)

# Suffix
tk.Label(root, text="Suffix:").grid(row=2, column=0, padx=10, pady=10)
suffix_var = tk.StringVar()
tk.Entry(root, textvariable=suffix_var).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Pick Suffix", command=pick_suffix).grid(row=2, column=2, padx=10, pady=10)

# Pick Both Button
tk.Button(root, text="Pick Both", command=pick_both).grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
