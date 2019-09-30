# Dictionary for different species of fish.
fish = {'Tangs': ['Yellow','Kole', 'Blue', 'Powder Blue', 'Powder Brown', 'Naso',
'Blonde Naso', 'Sailfin', 'Scopas', 'Clown', 'Convict', 'Achilles', 'Purple','Chevron', 'Lieutenant',
'Yellow Belly Blue Regal', 'Blue Carribean', 'Gemmatum','Black Longnose', 'Two Spot Bristletooth', 'Orange Shoulder',
'Square Tail Bristletooth','Whitetail Bristletooth', 'Mimic Lemon Peel', 'Vlamingii'],

'Dragonets':['Green Mandarin', 'Spotted Mandarin', 'Red Mandarin', 'Scooter Blenny', 'Ruby Red Dragonet', 'Red Scooter Dragonet'],
'Chromis':['Blue/Green Reef','Black Axil','Lemon','Blue Reef','Black & White','Agile','Sunshine Purple & Yellow','Webers'],
'Clowns':[],
'Gobies':[],
'Angel':[],
'Dwarf Angel':[],
'Anglers':[],
'Anthias':[],
'Basslets':[],
'Blennies':[],
'Butterfly':[],
'Boxfish':[],
'Cardinal':[],
'Damsel':[],
'Dottyback':[],
'Hawkfish':[],
'Wrasse Reef Safe':[],
'Wrasse Fish Only':[],
'Dartfish':[],
'Puffers':[],
'Lionfish':[],
'Rays':[],
'Eels':[],
'Foxface & Rabbit':[],
'Filefish':[],
'Groupers':[],
'Hogfish':[],
'Jawfish':[],
        }
# Dictionary for different species of coral.
coral = {'LPS':[],'SPS':[],'Soft':[],'Mushrooms':[],'Polyp':[],}
# Dictionary for different species of invertebrates.
inverts = {'Anemones':['Bulb','Long Tentacle','Ritteri','Sebae','Haddons Green Carpet','Condy','Haitian Reef','Tube',
'Long Purple Tentacle','True Tan Carpet','Mini Carpet','Rose Bulb'],'Crabs':['Dwarf Red Tip Hermit','Dwarf Blue Leg Hermit',
'Scarlet Reef Hermit','Dwarf Yellow Tip Hermit','Dwarf Zebra/Orange & Black Hermit','Emerald','Arrow','Decorator Arrow',
'Panamic','Electric Blue Hermit','Electric Orange Hermit','Halloween Hermit','Hermit w/ Anemone','Pom Pom','Sally Lightfoot',
'Spider Decorator','Trapezia Acropora','Staghorn'],'Cucumbers':['Sea Tiger Tail','Sea','Sea Yellow',
'Spiny Green w/Pink & Yellow'],'Fan Worms':['Hawaiian Feather Duster','Dwarf Colored Feather Duster','Feather Duster',
'Hard Tube Coco','Christams Tree on Rock'],'Lobsters':['Daums Reef','Debelius Reef'],'Shrimp':['Scarlet Skunk Cleaner',
'Peppermint','Blood Red Fire','Sexy Anemone','Banded Coral','Camel','Curly-Que','Yellow Banded Coral','Saron',
'White Spot Anemone','Harequin','Blue Banded Coral','Bumble Bee','Red Banded Snapping','Gold Banded Coral','Pederson Cleaner',
'Venus Anemone','Yellow Line'],'Sea Stars':['Burgundy Sea','Red Sea','Orange/Red Tile Sea','Indian Sea','Fancy Yellow Brittle Sea',
'Red Brittle Sea','Fancy Brittle Sea','Banded Brittle Sea','Fancy Tiger Striped Serpent Sea','Fancy Banded Serpent Sea',
'Fancy Red Brittle Sea','Knobby Fancy Brittle Sea','Red Knob Sea','Chocolate Chip Sea','Linckia Sea','Sand Sifting Sea'],
'Sea Slugs':['Blue Velvet Nudibranch','Green Lettus Sea','Sea Hare'],'Snails':['Astaea Turbo','Banded Trochus','Cerith',
'Margarita','Super Tongan Nassarius','Zebra Turbo','Abalone','Bumble Bee','Nerite','Spiny Star Astraea','Tiger Cowrie',
'Fighting Conch','Mexican Turbo','Nassarius','Turban','Chestnut Turbo','Chestnut Cowrie'],'Urchins':['Blue Tuxedo','Pincushion',
'Black Longspine','Hairy Pincushion','Pencil','Banded Longspine','Blue Spot Longspine','Purple Shortspine Pincushion',
'Red Tuxedo','Shortspine'],'Sponges':['Red Ball','Tree','Yellow Ball'],'Clams':['Maxima','Maxima Ultra',
'Striped with Blue Rim Derasa','Gold Maxima','Blue/Turquoise Maxima','Crocea','Blue Squamosa'],
'Cephalopods':['Atlantic Pygmy Octopus','Octopus-Assorted'],'Plants & Algae':['Red Mangrove','Red Gracilaria Feeding',
'Dragons Tongue','Shaving Brush','Mermaids Fan','Halimeda','Green Finger','Chaeto','Caulerpa'],
'Scallops':['Electric Flame']}


print("What type of fish do you want to view?")
name = input()

for name, types in fish.items():
    fish['Tangs'].sort()
    fish['Chromis'].sort()
    fish['Dragonets'].sort()
    print("\n" + name.title())
    for type in types:
        print("\t" + type.title())
#if type not in fish.keys():
#    print("Fish not found")
#else:
#for type in fish.key():
#    print("\t" + type)
# Print Tangs.
#for Tangs in fish['Tangs']:
#    fish['Tangs'].sort()
#    print("\t" + Tangs)
