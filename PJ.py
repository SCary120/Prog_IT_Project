# Nested dictionary for different species of fish.
fish = {
# Dictionary of Tangs fish.
"Tangs": {"Yellow":{"Care Level:" : "Easy", "Temperament" : "Semi-Aggressive" , "Origin" : "Hawaii", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "100 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Kole": {"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" , "Origin" : "Hawaii", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "70 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Blue":{"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" , "Origin" : "Fiji, Indonesia, Maldives ", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Powder Blue":{"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" , "Origin" : "Africa, Maldives ", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "125 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}, "Powder Brown":{"Care Level:" : "Moderate",
"Temperament" : "Semi-Aggressive" , "Origin" : "Phillipines", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "125 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}, "Naso":{"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" ,
"Origin" : "Fiji, Hawaii, Indonesia, Phillipines, Sri Lanka, Tonga", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},"Blonde Naso":{"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" ,
"Origin" : "Maldives", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}, "Sailfin":{"Care Level:" : "Moderate", "Temperament" : "Semi-Aggressive" ,
"Origin" : "Fiji, Indonesia, Sumatra", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}, "Scopas":{"Care Level:" : "Moderate",
"Temperament" : "Semi-Aggressive" , "Origin" : "Fiji, Indonesia, Phillipines", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "125 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},"Clown":{"Care Level:" : "Difficult", "Temperament" : "Semi-Aggressive" ,
"Origin" : "Fiji, Maldives, New Caledonia", "Diet": "Herbivore", "Reef Compatible" : "Yes", "Minimum Tank Size" : "250 gallons",
"Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Convict":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Africa, Fiji, Indonesia, Solomon Islands, Sri Lanka, Tahiti", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "125 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Achilles":{"Care Level:" : "Difficult", "Expert Only" : "Semi-Aggressive" , "Origin" : "Hawaii", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Purple":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Kenya, Red Sea", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "125 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Chevron":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Christmas Island", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Lieutenant":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Indonesia, Maldives", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Yellow Belly Blue Regal":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Kenya, Maldives", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Blue Carribean":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Caribbean", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Gemmatum":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Madagascar", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Black Longnose":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Christmas Island", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Two Spot Bristletooth":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Africa, Fiji, New Caledonia, Sumatra", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "70 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Orange Shoulder":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Fiji, Indonesia, New Caledonia", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "180 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Square Tail Bristletooth":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Africa, Sri Lanka", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "70 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Whitetail Bristletooth":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Tahiti", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "70 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Mimic Lemon Peel":{"Care Level:" : "Difficult", "Easy" : "Semi-Aggressive" , "Origin" : "Fiji, Indonesia, Sri Lanka", "Diet": "Herbivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "125 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Vlamingii":{"Care Level:" : "Difficult", "Moderate" : "Semi-Aggressive" , "Origin" : "Indonesia", "Diet": "Herbivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "360 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}},
# Dictionary of Dragonets fish.
"Dragonets":{"Green Mandarin":{ "Care Level:" : "Difficult", "Temperament" : "Peaceful" , "Origin" : "Phillipines", "Diet": "Carnivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, pH: 8.1-8.4, Salinity: 1.020-1.025, dKH: 8-12"},
"Spotted Mandarin":{ "Care Level:" : "Difficult", "Moderate" : "Peaceful" , "Origin" : "Indo Pacific", "Diet": "Carnivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Red Mandarin":{"Care Level:" : "Difficult", "Moderate" : "Peaceful" , "Origin" : "Phillipines", "Diet": "Carnivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Scooter Blenny":{"Care Level:" : "Difficult", "Moderate" : "Peaceful" , "Origin" : "Fiji, Indonesia, Solomon Islands", "Diet": "Carnivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Ruby Red Dragonet":{"Care Level:" : "Difficult", "Moderate" : "Peaceful" , "Origin" : "Phillipines", "Diet": "Carnivore", "Reef Compatible" : "Yes",
"Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"},
"Red Scooter Dragonet":{"Care Level:" : "Difficult", "Moderate" : "Peaceful" , "Origin" : "Maldives, Sri Lanka", "Diet": "Carnivore",
"Reef Compatible" : "Yes", "Minimum Tank Size" : "30 gallons", "Water Conditions" : "Temp: 72-78 degrees, Salinity: 1.020-1.025, pH: 8.1-8.4, dKH: 8-12"}}}




# Dictionary of Chromis fish.    
"Chromis":{"1":"Blue/Green Reef","2":"Black Axil","3":"Lemon","4":"Blue Reef","5":"Black & White",
"6":"Agile","7":"Sunshine Purple & Yellow","8":"Webers"},
# Dictionary of clown fish.    
"Clowns":{"1":"Mocha Black Storm","2":"Black Storm","3":"Latezonatus","4":"Ocellaris","5":"Picasso Percula","6":"Semi Picasso","7":"Wyoming White",
"8":"Davinci","9":"MochaVinci","10":"Wide Bar Mocha Gladiator","11":"Clarkii","12":"Black & White Ocellaris","13":"Snow Onyx","14":"Black Onyx",
"15":"Snowflake Ocellaris","16":"Black Snowflake Phantom","17":"Maine Blizzard","18":"Flurry","19":"Frostbite","20":"Black Ice","21":"Black Photon",
"22":"Naked","23":"Nearly Naked","24":"Midnight Ocellaris","25":"Domino","26":"Maroon","27":"Gold Nugget","28":"Gold Dot","29":"Lightning Maroon",
"30":"Thunder Maroon","31":"YellowstripeMaroon","32":"Cinnamon","33":"Spotcinctus","34":"Pink Skunk","35":"Red Saddle","36":"Tomato",
"37":"Fiji Barberi","38":"Galaxy Clarkii","39":"Pearl Eye Clarkii","40":"Two Banded","41":"Saddleback"},
# Dictionary of Gobies fish.
"Gobies":{"1":"Yello Prawn","2":"Court Jester","3":"Diamond Watchman","4":"Pink Spotted","5":"Tiger Watchman","6":"Hi Fin Red Banded","7":"Sleeper Banded",
"8":"Sleeper Blue Dot","9":"Sleeper Gold Head","10":"Yellow Clown","11":"Green Clown","12":"Black Clown","13":"Wheelers Shrimp","14":"Bella",
"15":"Flagtail Shrimp","16":"Bluespotted Watchman","17":"Greenbanded","18":"Sleeper Railway Glider","19":"Sleeper Striped","20":"Citrinis Clown",
"21":"Red Neon Eviota","22":"Yasha White Ray Shrimp","23":"Wide-barred Shrimp","24":"Orange Stripe Prawn","25":"Neon Blue","26":"Gold Neon Eviota",
"27":"Two Spot","28":"Orange Spotted","29":"Engineer","30":"Hectors","31":"Pinkbar","32":"Red Head","33":"Cave Transparent","34":"Steinitz",
"35":"Orangemarked","36":"Tangaroa","37":"Panda","38":"Masked","39":"Black Barred Convict","40":"Yellow Priolepis","41":"Dracula","42":"Decorated",
"43":"Broadstripe"},
#Dictionary of Angel fish.
"Angel":{"1":"Asfur","2":"Blue Girdled","3":"Blueline","4":"Goldflake","5":"Regal","6":"Bellus","7":"Scribbled","8":"Passer","9":"Koran",
"10":"Emperor","11":"Queen","12":"Blueface","13":"Annularis","14":"French","15":"Rock Beauty","16":"Spotbreast","17":"Lamarcks","18":"Watanabei",
"19":"Singapore","20":"Gray","21":"Xanthurus Cream","22":"Flagfin","23":"False Personifer","24":"Chrysurus","25":"Maculosus","26":"Cortez",
"27":"Zebra Lyretail"},
# Dictionary of Dwarf Angel Fish.    
"Dwarf Angel":{"1":"Flame","2":"Coral Beauty","3":"Yellow","4":"Tibicen","5":"Joculator","6":"True Shepards","7":"Bicolor",
"8":"Lemonpeel","9":"Yellowfin","10":"Flameback","11":"Collins","12":"Potters","13":"Red Stripe","14":"Rusty","15":"Half Black","16":"Bluefin","17":"Pygmy",
"18":"Black Nox","19":"Multicolor","20":"Golden"},
# Dictionary of Angler fish.    
"Anglers":{"1":"Assorted","2":"Wartskin","3":"Red/Orange","4":"Sargassum"},
# Dictionary of Anthia fish.    
"Anthias":{"1":"Dispar","2":"Bartlett","3":"Lyretail","4":"Indian Ocean Lyretail","5":"Carberryi","6":"Stocky","7":"Evansi","8":"Sunset",
"9":"Pictilis","10":"Ignitus","11":"Squareback","12":"Resplendent","13":"Randalls","14":"Huchtii","15":"Red Belted","16":"Bimaculatus","17":"Fathead Sunburst",
"18":"Red Saddled","19":"Princess","20":"Waitei","21":"Loris","22":"Red Fairy","23":"Bali Lunate","24":"Red-Bar"}, 
# Dictionary of Basslet fish.    
"Basslets":{"1":"Royal Gramma","2":"Chalk Bass","3":"Lantern Bass","4":"Tobacco","5":"Harlequin","6":"Black Cap","7":"Gold Assessor"},
# Dictionary of Blenny fish.
"Blennies":{"1":"Sailfin/Algae","2":"Bicolor","3":"Midas","4":"Tail Spot","5":"Linear","6":"Two Spot","7":"Black Sailfin","8":"Starry",
"9":"Black Combtooth","10":"Canary","11":"Green Canary","12":"Forktail","13":"Yellow Eye Combtooth","14":"Segmented Sailfin","15":"One Spot",
"16":"Striped","17":"White","18":"Harptail","19":"Black-Lined","20":"Ember","21":"Bundoon","22":"Brachiosaurus","23":"Eyebrow"},
# Dictionary of Butterfly fish.       
"Butterfly":{"1":"Auriga","2":"Four Eyed","3":"Pakistan","4":"Declivis","5":"Saddleback",
"6":"Falcula","7":"Raccoon","8":"Orange","9":"Mertensii","10":"Spotfin","11":"Sunset","12":"Latticed","13":"Banded","14":"Tahitian","15":"Double Saddle",
"16":"Tear Drop","17":"Vagabond","18":"Pearlscale","19":"Copperband","20":"Yellow Longnose","21":"Zoster","22":"Heniochus","23":"Red Sea",
"24":"Singular","25":"Hi Fin Coradion","26":"Indian Vegabond","27":"Yellowhead"},
# Dictionary of Boxfish.    
"Boxfish":{"1":"Longhorn Cowfish","2":"Cubicus"},
# Dictionary of Cardinal fish.    
"Cardinal":{"1":"Pajama","2":"Red Belted","3":"Longspine","4":"Yellowstriped","5":"Flame","6":"Fowleria","7":"Ochrestriped","8":"Five Lined",
"9":"Yellow","10":"Bangai"},
# Dictionary of Damsel fish.    
"Damsel":{"1":"Ambon","2":"Yellowtail","3":"Azure","4":"Blue","5":"Blue Sapphire","6":"Three Spot Domino","7":"Four Stripe",
"8":"Three Stripe","9":"Fiji Blue Devil","10":"Two Stripe","11":"Blue and Gold","12":"Talbots","13":"Blue Velvet","14":"Pink Smith","15":"Neon",
"16":"Rollands","17":"Regal","18":"Similar","19":"Traceys"},
# Dictionary of Dottyback fish.    
"Dottyback":{"1":"Pruple","2":"Purple Stripe","3":"Bicolor","4":"Splendid","5":"Whitetail",
"6":"Ring Eyed","7":"Yellow","8":"Red Spotted","9":"Neon","10":"Springeri","11":"Double Striped","12":"Blue Eye Royal","13":"Orangetail",
"14":"Red Elongated","15":"Black Neon","16":"Splendid"},
# Dictionary of Hawkfish.    
"Hawkfish":{"1":"Falco","2":"Flame","3":"Pixy/Spotted","4":"Longnose",
"5":"Arc Eye","6":"Freckled","7":"Red","8":"Blood Red"},
# Dictionary of Wrasse that are Reef safe.    
"Wrasse Reef Safe":{"1":"Darwins Glow","2":"Magma Fairy","3":"Splendid Pintail",
"4":"Katherines Fairy","5":"Lunate Fairy","6":"Ornate Leopard","7":"Blue Throat","8":"Naokos Fairy","9":"Rose-Band Fairy","10":"Red-Fin Fairy",
"11":"Redfin","12":"Leopard","13":"Black Leopard","14":"Four Line","15":"Six Line","16":"Hooded Fairy","17":"Orange-Back Fairy","18":"Ruby Head Fairy",
"19":"Scotts Fairy","20":"Bluehead Fairy","21":"Exquisite Fairy","22":"Whip Fin Fairy","23":"Yellow Fin Fairy","24":"Johnsons Fairy","25":"Flame Fairy",
"26":"Labouts Fairy","27":"Lineatus Fairy","28":"Multicolor Lubbocks Fairy","29":"Yellow-Flanked Fairy","30":"Fine Spotted Fairy",
"31":"Golden Rhomboidalis","32":"Pink Margin Fairy","33":"Red Velvet Fairy","34":"Red Head Solon Fairy","35":"Pearly Wrasse","36":"Bluestreak Cleaner",
"37":"Ruby Longfin Fairy","38":"McCoskers Flasher","39":"Carpenters Flasher","40":"Yellowfin Flasher","41":"Blue Flasher","42":"Linespot Flahser",
"43":"Filamented Flasher","44":"Mystery","45":"Yellowband","46":"Pink-Streaked","47":"Scarlet Pin Stripe","48":"Eight Lined"},
# Dictionary of Foxface & Rabbit fish.    
"Foxface & Rabbit":{"1":"Foxface Lo","2":"One Spot Foxface","3":"Magnificent Foxface","4":"Yellow Blotch Rabbit","5":"Blue Spotted Rabbit",
"6":"Two Barred Rabbit","7":"Decorated Rabbit","8":"Gold Spotted Rabbit","9":"Bicolor Fox"},
# Dictionary of Filefish.    
"Filefish":{"1":"Aiptasia Eating","2":"Tassle"},
# Dictionary of Grouper fish.    
"Groupers":{"1":"Blue Line","2":"Miniatus","3":"Pollenei"},"Hogfish":{"1":"Yellow Candy","2":"Spanish","3":"Axilspot","4":"Red Diana","5":"Coral"},
# Dictionary of Jawfish.    
"Jawfish":{"1":"Blue Dot","2":"Yellowhead","3":"Black Cap","4":"Chinstrap"},
# Dictionary of Wrasse for fish only environment.    
"Wrasse Fish Only":{"1":"Harlequin Tusk","2":"Yellow","3":"Yellow & Purple",
"4":"Green","5":"Red Coris","6":"Formosa","7":"Melanurus","8":"Radiant","9":"Christmas","10":"Vroliks","11":"Marble/Hortulanus","12":"Grey Head",
"13":"Adorned","14":"Lyretail","15":"Bluehead","16":"Banana","17":"Bird","18":"Dragon","19":"Hardwicke","20":"Paddlefin","21":"Pinkface","22":"Neon",
"23":"Goldbar","24":"Blunthead","25":"Red Breast","26":"Black-backed","27":"Red-Lined","28":"Two Spot","29":"Dusky","30":"Two Tone","31":"Richmonds",
"32":"Jansen Saddle","33":"Sea Grass","34":"Redtail Hawaii"},
# Dictionary of Dartfish    
"Dartfish":{"1":"Firefish","2":"Purple Firefish","3":"Scissortail","4":"Zebra Barred","5":"Blue Gudgeon","6":"Exquisite Firefish",
"7":"Helfrichi Firefish"},
# Dictionary of Puffer fish.    
"Puffers":{"1":"Saddle Valentini","2":"Porcupine","3":"Arothron","4":"Arothron Dog Face","5":"Saddle","6":"Scribbled Arothron","7":"Spiny Box",
"8":"Blue Spotted","9":"Spotted","10":"Central American Sharpnose","11":"Leopard","12":"Bennetts Sharpnose","13":"Immaculatus","14":"Narrow-Lined",
"15":"Stars & Stripes","16":"Reticulated"},
# Dictionary of Lionfish    
"Lionfish":{"1":"Dwarf/Zebra","2":"Fuzzy Dwarf","3":"Colored Volitan","4":"Miles","5":"Antennata","6":"Radiata","7":"Russells","8":"Mombasa"},
# Dictionary of Eels.    
"Eels":{"1":"Golden Dwarf Moray","2":"Snowflake","3":"Tessalata","4":"Wolf","5":"Zebra Moray","6":"Golden Banana Moray","7":"Black Edge Moray",
"8":"Jeweled Moray","9":"Japanese Dragon","10":"Yellow-Edged"}
}
# Nested Dictionary for Coral.
coral = {
# Dictionary of LPS coral.
"LPS":{"Lobophyllia sp.":{}, "Homophyllia australis":{}, "Acanthophyllia desshayesiana":{}, "Plesiastrea versipora":{}, "Trachyphyllia geoffroyi":{},
"Favia sp":{}, "Plerogyra sinuosa":{}, "Favia speciosa":{}, "Favites spp.":{}, "Lobophyllia hemprichii":{}, "Platygyra sp.":{}, "Acanthastrea echinata":{},
"Micromussa lordhowensis":{}, "Goniastrea sp.":{}, "Fungia repanda":{}, "Fungia sp":{}, "Blastomussa merletti":{}, "Catalaphyllia jardinei":{}, "Caulastrea furcata":{},
"Echinophyllia sp.":{}, "Echinophyllia aspera":{}, "Duncanopsammia axifuga":{}, "Euphyllia ancora":{}, "Euphyllia glabrescens":{}, "Euphyllia divisa":{}, "Cynarina lacrymalis":{},
"Parascolymia vitiensis":{}, "Gonipora sp.":{},"Galaxea spp.":{}, "Balanophyllia sp.":{}, "Favites pentagona":{}, "Merulina ampliata":{}, "Physogyra sp.":{},
"Tubastrea micrantha":{}, "Turbina sp.":{}, "Euphyllia cristata":{}, "Homophyllia bowerbanki":{}, "Euphyllia parancora":{}, "Turbinaria peltata":{}, "Blastomussa wellsi":{},
"Polyphyllia sp.":{}, "Caulastrea echinulata":{}, "Tubastrea sp.":{}, "Tubastrea aurea":{}, "Euphyllia yaeyamaensis":{}, "Diploastrea heliopora":{}, "Trachyphyllia radiata":{},
"Mycedium sp.":{}, "Caulastrea curvata":{}, "Pectinia sp.":{}, "Heliofungia actinifomis" :{}, "Turbinaria sp.":{}, "Alveopora sp.":{}},
# Dictionary of SPS coral.
"SPS":{"Acropora sp.":{}, "Montipora nodosa":{}, "Pavona maldivensis":{}, "Montipora verrucosa":{}, "Seriatopra hystrix":{}, "Porites spp.":{},
"Stylophora spp.":{}, "Pocillopora damicornis":{}, "Acropora millepora":{}, "Heliopora coerulea":{}, "Hydophora sp.":{}, "Hydnophora exesa":{},
"Montipora digitata":{}, "Montipora capricornis":{}, "Pavona decussatus":{}, "Pachyseris sp.":{}},
# Dictionary of Soft coral
"Soft":{"Sinularia sp.":{}, "Sarcophyton sp.":{}, "Lobophytum sp.":{}, "Rhodactis sp.":{}, "Tubipora musica":{}, "Sympodium sp.":{},
"Sarcophyton elegans":{}, "Capnella sp.":{}, "Paralemnalia sp.":{}, "Sinularia brassica":{}, "Sinularia flexibilis":{},
"Sphaerella sp.":{}, "Heliopora coerulea":{}, "Stereonephthya sp.":{}, "Nephthyigorgia sp.":{}, "Dendronephthya sp.":{}, "Clavularia sp.":{},
"Briareum sp.":{}, "Xenia sp.":{}, "Knopia sp.":{}, "Litophyton sp.":{}},
# Dictionary of mushroom coral.
"Mushrooms":{"Actinodiscus sp.":{}, "Rhodactis inchoata":{}, "Rhodactis sp.":{}, "Rhodactis indosinensis":{}, "Ricordea yuma":{}},
# Dictionary of Polyp coral
"Polyp":{"Zoanthus sp.":{}, "Tubipora musica":{}, "Sympodium sp.":{}, "Undescribed Zoanthid":{}, "Xenia sp.":{}, "Knopia sp.":{}, "Clavularia sp.":{},
"Briareum sp.":{}}}

# Nested dictionaries of Inverts
inverts = {
# Dictionary of Anemones.
"Anemones":{"Bulb":{}, "Long Tentacle":{}, "Ritteri":{}, "Sebae":{}, "Haddons Green Carpet":{}, "Condy":{}, "Haitian Reef":{}, "Tube":{}, 
"Long Purple Tentacle":{}, "True Tan Carpet":{}, "Mini Carpet":{}, "Rose Bulb":{}},
# Dictionary of Crabs.
"Crabs":{"Dwarf Red Tip Hermit":{}, "Dwarf Blue Leg Hermit":{}, "Scarlet Reef Hermit":{}, "Dwarf Yellow Tip Hermit":{}, "Dwarf Zebra/Orange & Black Hermit":{}, 
"Emerald":{}, "Arrow":{}, "Decorator Arrow":{}, "Panamic":{}, "Electric Blue Hermit":{}, "Electric Orange Hermit":{}, "Halloween Hermit":{}, 
"Hermit w/ Anemone":{}, "Pom Pom":{}, "Sally Lightfoot":{}, "Spider Decorator":{}, "Trapezia Acropora":{}, "Staghorn":{}},
# Dictionary of Sea Cucumbers.
"Cucumbers":{"Sea Tiger Tail":{}, "Sea":{}, "Sea Yellow":{}, "Spiny Green w/Pink & Yellow":{}},
# Dictionary of Fan Worms.
"Fan Worms":{"Hawaiian Feather Duster":{}, "Dwarf Colored Feather Duster":{}, "Feather Duster":{}, "Hard Tube Coco":{}, "Christams Tree on Rock":{}},
# Dictionary of Lobsters.
"Lobsters":{"Daums Reef":{}, "Debelius Reef":{}},
# Dictionary of Shrimp.
"Shrimp":{"Scarlet Skunk Cleaner":{}, "Peppermint":{}, "Blood Red Fire":{}, "Sexy Anemone":{}, "Banded Coral":{}, "Camel":{}, "Curly-Que":{}, 
"Yellow Banded Coral":{}, "Saron":{}, "White Spot Anemone":{}, "Harlequin":{}, "Blue Banded Coral":{}, "Bumble Bee":{}, "Red Banded Snapping":{}, 
"Gold Banded Coral":{}, "Pederson Cleaner":{}, "Venus Anemone":{}, "Yellow Line":{}},
# Dictionary of Sea Stars.
"Sea Stars":{"Burgundy Sea":{}, "Red Sea":{}, "Orange/Red Tile Sea":{}, "Indian Sea":{}, "Fancy Yellow Brittle Sea":{},
"Red Brittle Sea":{}, "Fancy Brittle Sea":{}, "Banded Brittle Sea":{}, "Fancy Tiger Striped Serpent Sea":{}, "Fancy Banded Serpent Sea":{}, 
"Fancy Red Brittle Sea":{}, "Knobby Fancy Brittle Sea":{}, "Red Knob Sea":{}, "Chocolate Chip Sea":{}, "Linckia Sea":{}, "Sand Sifting Sea":{}},
# Dictionary of Sea Slugs.
"Sea Slugs":{"Blue Velvet Nudibranch":{}, "Green Lettus Sea":{}, "Sea Hare":{}},
# Dictionary of Snails.
"Snails":{"Astaea Turbo":{}, "Banded Trochus":{}, "Cerith":{}, "Margarita":{}, "Super Tongan Nassarius":{}, "Zebra Turbo":{}, "Abalone":{}, "Bumble Bee":{},
"Nerite":{}, "Spiny Star Astraea":{}, "Tiger Cowrie":{}, "Fighting Conch":{}, "Mexican Turbo":{}, "Nassarius":{}, "Turban":{}, "Chestnut Turbo":{}, "Chestnut Cowrie":{}},
# Dictionary of Urchins.
"Urchins":{"Blue Tuxedo":{}, "Pincushion":{}, "Black Longspine":{}, "Hairy Pincushion":{}, "Pencil":{}, "Banded Longspine":{}, "Blue Spot Longspine":{}, 
"Purple Shortspine Pincushion":{}, "Red Tuxedo":{}, "Shortspine":{}},
# Dictionary of Sponges.
"Sponges":{"Red Ball":{}, "Tree":{}, "Yellow Ball":{}},
# Dictionary of Clams.
"Clams":{"Maxima":{}, "Maxima Ultra":{}, "Striped with Blue Rim Derasa":{}, "Gold Maxima":{}, "Blue/Turquoise Maxima":{}, "Crocea":{}, "Blue Squamosa":{}},
# Dictionary of Cephalopods.
"Cephalopods":{"Atlantic Pygmy Octopus":{}, "Octopus-Assorted":{}},
# Dictionary of Plants & Macro Algae.
"Plants & Algae":{"Red Mangrove":{}, "Red Gracilaria Feeding":{}, "Dragons Tongue":{}, "Shaving Brush":{}, "Mermaids Fan":{}, "Halimeda":{}, 
"Green Finger":{}, "Chaeto":{}, "Caulerpa":{}},
# Dictionary of Scallops.
"Scallops":{"Electric Flame":{}}}

# import csv module to read and write to csv.
import csv
# import datetime module so I can add date to CSV file for water parameters.
import datetime
#import termcolor to manipulate color of text.
from termcolor import colored, cprint

# function that will execute my program.
def program_start():
    # Welcome message that will explain options to the user.
    print(colored("Welcome to Steve's Reef Database!  A program designed to view information about different fish, coral and invertebrae."
      "\nYou can also use this program to log and track your water parameters! \nWhat would you like to do?\n\nSelect a number: ",'blue'))

    print(colored("1: View Fish, 2: View Coral, 3: View Inverts, 4: Log Water Parameters", 'yellow'))
    # Variable that will be used in If/Elif loops below.  Stores user input, executes program based on selection.
    choice = input()
    # If user choice is to view fish, execute for loop below.
    if choice == "1":
        for i in fish:
            print(i)
        print("\nWhich fish would you like to view?")
        choice1 = input()
        if choice1 in fish:
            for i in fish[choice1]:
                print(i)
            print("\nWhich "+ choice1 + " would you like to view?")
        choice2 = input()
        if choice2 in fish[choice1]:
            for i in fish[choice1][choice2]:
                print(i,":",fish[choice1][choice2][i])
    # If user choice is to view coral, execute for loop below.
    elif choice == "2":
       for i in coral:
          print(i)
       print("\nWhich coral would you like to view?")
       choice1 = input()
       if choice1 in coral:
           for i in coral[choice1]:
               print(i)
           print("\nWhich "+ choice1 + " would you like to view?")
       choice2 = input()
       if choice2 in coral[choice1]:
            for i in coral[choice1][choice2]:
                print(i,":",coral[choice1][choice2][i])
    # If user choice is to view inverts, execute for loop below.
    elif choice == "3":
       for i in inverts:
           print(i)
       print("\nWhich invertebrae would you like to view?")
       choice1 = input()
       if choice1 in inverts:
           for i in inverts[choice1]:
               print(i)
           print("\nWhich "+ choice1 + " would you like to view?")
       choice2 = input()
       if choice2 in inverts[choice1]:
            for i in inverts[choice1][choice2]:
                print(i,":",inverts[choice1][choice2][i])


# call the function to start the program.
program_start()

# function to read csv file containing water parameters.     
def read_reef():

    reef = csv.reader(open("steve.csv", newline=''))
    for row in reef:
        print('{:<12} {:<10} {:<12} {:<10} {:<8} {:<8} {:<10} {:<10} {:<12} {:<10} {:<16} {:<10}'.format(*row))

# call the function to read the csv file.
read_reef()
