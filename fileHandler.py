import json, os
import AppData.GlobalVars as GV

# Load expedition names from the NightreignData directory
def loadExpeditions():
    expeditions = ["Choose Expedition"]
    for f in os.listdir(GV.EXPEDITION_DATA_PATH):
        expeditions.append(f[:-5])  # Remove .json extension
    return expeditions

def parseJson(choice):
    # Open the JSON file and pass the file object directly to json.load
    with open(f"{GV.EXPEDITION_DATA_PATH}/{choice}.json", "r", encoding="utf-8") as f:
        bossDataJson = json.load(f)
    
        listOfBossDicts = []

        # Parse each boss's data and format it into a dictionary because of the damn Sentient Pest
        for i, boss in enumerate(bossDataJson["bosses"]):
            bossNameStr = bossDataJson["bosses"][i]["bossName"]
            resistantTo = bossDataJson["bosses"][i]["strongAgainst"]
            weakTo = bossDataJson["bosses"][i]["weakAgainst"]
            resistantStr = ", ".join(resistantTo) if resistantTo else "None"
            weakStr = ", ".join(weakTo) if weakTo else "None"
            resistances = bossDataJson["bosses"][i]["resistances"]
            negations = bossDataJson["bosses"][i]["negations"]
            resistancesStr = "\n"
            negationsStr = "\n"

            #IDK MAN IT WORKS Takes care of resistances dictionary
            for status, values in resistances.items():
                valueStr = ''
                if values is None:
                    valueStr = 'Immune '
                else:
                    for value in values:
                        valueStr += f'{value}/'
                
                resistancesStr += f'{GV.RESISTANCE_NAMES.get(status, status)}: {valueStr[:-1]}\n'


            #IDK MAN IT WORKS Takes care of negations dictionary
            for status, values in negations.items():
                negationsStr += f'{GV.NEGATION_NAMES.get(status, status)}: {values}\n'
            
            damage = bossDataJson["bosses"][i]["damage"]
            damageStr = ", ".join(damage) if damage else "None"
            inflicts = bossDataJson["bosses"][i]["inflicts"]
            inflictsStr = ", ".join(inflicts) if inflicts else "None"
            sttanceStr = bossDataJson["bosses"][i]["stance"]

            bossDataDict = {
                'bossName': bossNameStr,
                'resistant': resistantStr,
                'weak': weakStr,
                'resistances': resistancesStr,
                'negations': negationsStr,
                'damage': damageStr,
                'inflicts': inflictsStr,
                'stance': sttanceStr
            }

            listOfBossDicts.append(bossDataDict)

        return listOfBossDicts
 