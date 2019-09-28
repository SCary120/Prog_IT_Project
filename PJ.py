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
inverts = {'Anemones':[],'Crabs':[],'Cucumbers':[],'Fan Worms':[],'Lobsters':[],'Shrimp':[],'Sea Stars':[],'Sea Slugs':[],
'Snails':[],'Urchins':[],'Sponges':[],'Clams':[],'Cephalopods':[],'Algae':[]}



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
