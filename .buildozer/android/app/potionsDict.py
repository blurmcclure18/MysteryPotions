from random import randint

potions = {
    0:{'PotionName': 'Potion of Poison', 'PotionDescription': "If you drink it, you take 3d6 poison damage, and you must succeed on a DC 13 Constitution saving throw or be poisoned.\n\nAt the start of each of your turns while you are poisoned in this way, you take 3d6 poison damage. At the end of each of your turns, you can repeat the saving throw. On a successful save, the poison damage you take on your subsequent turns decreases by 1d6.\n\nThe poison ends when the damage decreases to 0." },
    
    1:{'PotionName': 'Potion of Resistance', 'PotionDescription': "When you drink this potion, you gain resistance to one type of damage for 1 hour.", 'Options': {1:'Potion of Acid Resistance', 2:'Potion of Cold Resistance', 3:'Potion of Fire Resistance', 4:'Potion of Force Resistance', 5: 'Potion of Lightning Resistance', 6: 'Potion of Necrotic Resistance', 7: 'Potion of Poison Resistance', 8: 'Potion of Psychic Resistance', 9: 'Potion of Radiant Resistance', 10: 'Potion of Thunder Resistance'}},
    
    2: {'PotionName': 'Potion of Speed', 'PotionDescription': "When you drink this potion, you gain the effect of the haste spell for 1 minute (no concentration required).\n\nThe potion's yellow fluid is streaked with black and swirls on its own."},
    
    3: {'PotionName': 'Potion of Gaseous Form', 'PotionDescription': "When you drink this potion, you gain the effect of the gaseous form spell for 1 hour (no concentration required) or until you end the effect as a bonus action.\n\nThis potion's container seems to hold fog that moves and pours like water."},
    
    4: {'PotionName': 'Potion of Growth', 'PotionDescription': "When you drink this potion, you gain the 'enlarge' effect of the enlarge/reduce spell for 1d4 hours (no concentration required). The red in the potion's liquid continuously expands from a tiny bead to color the clear liquid around it and then contracts. Shaking the bottle fails to interrupt this process."},
    
    5: {'PotionName': 'Potion of Healing', 'PotionDescription':"You regain hit points when you drink this potion. The number of hit points depends on the potion’s rarity, as shown in the Potions of Healing table. Whatever its potency, the potion’s red liquid glimmers when agitated.", 'Options': {1: "Potion of Healing (2d4 + 2)", 2: "Potion of Greater Healing (4d4 + 4)", 3: "Potion of Superior Healing (8d4 + 8)", 4: "Potion of Supreme Healing (10d4 + 20)"}},
    
    6: {'PotionName': 'Potion of Invisibility', 'PotionDescription': "This potion's container looks empty but feels as though it holds liquid. When you drink it, you become invisible for 1 hour. Anything you wear or carry is invisible with you. The effect ends early if you attack or cast a spell."},
    
    7: {'PotionName': 'Potion of Climbing ', 'PotionDescription': "When you drink this potion, you gain a climbing speed equal to your walking speed for 1 hour.\n\nDuring this time, you have advantage on Strength (Athletics) checks you make to climb.\n\nThe potion is separated into brown, silver, and gray layers resembling bands of stone. Shaking the bottle fails to mix the colors."},
    
    8: {'PotionName': 'Potion of Diminution', 'PotionDescription': "When you drink this potion, you gain the 'reduce' effect of the enlarge/reduce spell for 1d4 hours (no concentration required).\n\nThe red in the potion's liquid continuously contracts to a tiny bead and then expands to color the clear liquid around it. Shaking the bottle fails to interrupt this process."},
    
    9: {'PotionName': 'Potion of Fire Breath', 'PotionDescription': "After drinking this potion, you can use a bonus action to exhale fire at a target within 30 feet of you. The target must make a DC 13 Dexterity saving throw, taking 4d6 fire damage on a failed save, or half as much damage on a successful one. The effect ends after you exhale the fire three times or when 1 hour has passed. \nThis potion's orange liquid flickers, and smoke fills the top of the container and wafts out whenever it is opened."},
    
    10: {'PotionName': 'Potion of Giant Strength', 'PotionDescription':"When you drink this potion, your Strength score changes for 1 hour.\n\nThe potion has no effect on you if your Strength is equal to or greater than that score.\n\nThis potion's transparent liquid has floating in it a sliver of fingernail from a giant of the appropriate type.", 'Options':{1:"Potion of Hill Giant Strength (Str: 21)", 2:"Potion of Frost Giant Strength (Str: 23)", 3: "Potion of Stone Giant Strength (Str: 23)", 4:"Potion of Fire Giant Strength (Str: 25)", 5:"Potion of Cloud Giant Strength (Str: 27)", 6: "Potion of Storm Giant Strength (Str: 29)"}},
}

def getpotion():
    roll = randint(1,100)

    if roll > 1 and roll <= 50:
        num = 0
    elif roll > 50 and roll <= 55:
        num = 1
    elif roll > 55 and roll <= 60:
        num = 2
    elif roll > 60 and roll <= 65:
        num = 3
    elif roll > 65 and roll <=70:
        num = 4
    elif roll > 70 and roll <= 75:
        num = 5
    elif roll > 75 and roll <= 80:
        num = 6
    elif roll > 80 and roll <= 85:
        num = 7
    elif roll > 85 and roll <= 90:
        num = 8
    elif roll > 90 and roll <= 95:
        num = 9
    elif roll > 95 and roll <= 100:
        num = 10

    rolledPotionName = potions[num]['PotionName']
    rolledPotionDescription = potions[num]['PotionDescription'] 
    try:
        potionOptions = len(potions[num]['Options'])
        if potionOptions > 0:
            rolledPotionOptions = potions[num]['Options']
            optionsRoll = randint(1,len(rolledPotionOptions))
            rolledPotionName = f"{rolledPotionOptions[optionsRoll]}"
        else:
            pass
    except:
        pass