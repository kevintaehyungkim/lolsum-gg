import collections
import json
import requests

# Data Dragon Base URL
BASE_URL = "http://ddragon.leagueoflegends.com/cdn"

# All patch version ordered recent to least recent
PATCH_VERSIONS = "https://ddragon.leagueoflegends.com/api/versions.json"

CHAMPION_DATA_EXT = "/data/en_US/champion/"
CHAMPION_DATA_ALL_EXT = "/data/en_US/champion.json"
CHAMPION_LOADING_IMAGE_EXT = "/img/champion/loading/"
CHAMPION_SQUARE_IMAGE_EXT = "/img/champion/"

JSON_EXT = ".json"



# Riot Data Dragon API #

'''
Returns the STRING value of the most recent patch version
'''
def get_current_patch():
    response = requests.get(PATCH_VERSIONS).content.decode("utf-8")
    patch_versions = json.loads(response)
    return patch_versions[0]


'''
Returns a LIST of all available champions for the patch version
'''
def get_all_champions(patch_version):
    request_url = BASE_URL + '/' + patch_version + CHAMPION_DATA_ALL_EXT
    response = requests.get(request_url).content.decode("utf-8")

    champion_data_all = json.loads(response)["data"]

    champion_list = []
    for champion_name in champion_data_all:
        champion_list.append(champion_name)

    return champion_list


'''
Returns a DICTIONARY of relevant champion data for provided champion and patch version

Need champion name: champion num, stats, ability names, 
'''


'''
"stats":{"hp":530,"hpperlevel":88,"mp":375,"mpperlevel":70,"movespeed":325,"armor":22,"armorperlevel":3.5,"spellblock":30,"spellblockperlevel":0.5,"attackrange":550,"hpregen":4,"hpregenperlevel":0.55,"mpregen":8.5,"mpregenperlevel":0.65,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":2.5,"attackspeedperlevel":2.5,"attackspeed":0.625}
'''
def get_champion_data(champion_name, patch_version):
    request_url = BASE_URL + '/' + patch_version + CHAMPION_DATA_EXT + champion_name + JSON_EXTENSION
    response = requests.get(request_url).content.decode("utf-8")

    champion_data = collections.defaultdict()
    champion_data_raw = json.loads(response)["data"]

    champion_data["stats"] = champion_data_raw["stats"]
    

    

    return champion_data

# '''
# "3157":
# {
# "name":"Zhonya's Hourglass",
# "description":"<mainText><stats><attention> 65</attention> Ability Power<br><attention> 45</attention> Armor<br><attention> 10</attention> Ability Haste</stats><br><br> <active>Active -</active> <active>Stasis:</active> You become <status>Invulnerable</status> and <status>Untargetable</status> for 2.5 seconds, but are prevented from taking any other actions during this time (120s cooldown).</mainText><br>",
# "colloq":";zhg;zonyas",
# "plaintext":"Activate to become invincible but unable to take actions",
# "from":["3191","2420","3108"],"image":{"full":"3157.png",
# "sprite":"item1.png",
# "group":"item","x":432,"y":48,"w":48,"h":48},
# "gold":{"base":50,"purchasable":true,"total":2500,
# "sell":1750},"tags":["Armor","SpellDamage","Active","CooldownReduction","AbilityHaste"],
# "maps":{"11":true,"12":true,"21":true,"22":false},
# "stats":{"FlatMagicDamageMod":65,"FlatArmorMod":45},
# "effect":{"Effect1Amount":"0","Effect2Amount":"2.5","Effect3Amount":"120"},
# "depth":3},

# item  
# "stats":{

# "FlatHPPoolMod":0,
# "rFlatHPModPerLevel":0,
# "FlatMPPoolMod":0,
# "rFlatMPModPerLevel":0,
# "PercentHPPoolMod":0,
# "PercentMPPoolMod":0,
# "FlatHPRegenMod":0,
# "rFlatHPRegenModPerLevel":0,
# "PercentHPRegenMod":0,
# "FlatMPRegenMod":0,
# "rFlatMPRegenModPerLevel":0,
# "PercentMPRegenMod":0,
# "FlatArmorMod":0,
# "rFlatArmorModPerLevel":0,
# "PercentArmorMod":0,
# "rFlatArmorPenetrationMod":0,
# "rFlatArmorPenetrationModPerLevel":0,
# "rPercentArmorPenetrationMod":0,
# "rPercentArmorPenetrationModPerLevel":0,
# "FlatPhysicalDamageMod":0,
# "rFlatPhysicalDamageModPerLevel":0,
# "PercentPhysicalDamageMod":0,
# "FlatMagicDamageMod":0,
# "rFlatMagicDamageModPerLevel":0,
# "PercentMagicDamageMod":0,
# "FlatMovementSpeedMod":0,
# "rFlatMovementSpeedModPerLevel":0,
# "PercentMovementSpeedMod":0,
# "rPercentMovementSpeedModPerLevel":0,
# "FlatAttackSpeedMod":0,
# "PercentAttackSpeedMod":0,
# "rPercentAttackSpeedModPerLevel":0,
# "rFlatDodgeMod":0,
# "rFlatDodgeModPerLevel":0,
# "PercentDodgeMod":0,
# "FlatCritChanceMod":0,
# "rFlatCritChanceModPerLevel":0,
# "PercentCritChanceMod":0,
# "FlatCritDamageMod":0,
# "rFlatCritDamageModPerLevel":0,
# "PercentCritDamageMod":0,
# "FlatBlockMod":0,
# "PercentBlockMod":0,
# "FlatSpellBlockMod":0,
# "rFlatSpellBlockModPerLevel":0,
# "PercentSpellBlockMod":0,
# "FlatEXPBonus":0,
# "PercentEXPBonus":0,
# "rPercentCooldownMod":0,
# "rPercentCooldownModPerLevel":0,
# "rFlatTimeDeadMod":0,
# "rFlatTimeDeadModPerLevel":0,
# "rPercentTimeDeadMod":0,
# "rPercentTimeDeadModPerLevel":0,
# "rFlatGoldPer10Mod":0,
# "rFlatMagicPenetrationMod":0,
# "rFlatMagicPenetrationModPerLevel":0,
# "rPercentMagicPenetrationMod":0,
# "rPercentMagicPenetrationModPerLevel":0,
# "FlatEnergyRegenMod":0,
# "rFlatEnergyRegenModPerLevel":0,
# "FlatEnergyPoolMod":0,
# "rFlatEnergyModPerLevel":0,
# "PercentLifeStealMod":0,
# "PercentSpellVampMod":0}
# '''
# def get_item_data():

# item_response = ... "http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/item.json"
# item_data = collections.defaultdict()
# item_data_all = item_data_response["data"]

# for item_num, item_data_raw in item_data_all:
# item_name = item_data_raw["name"]
# item_data[item_name]["item_num"] = item_num
# item_data[item_name]["gold"] = item_data_raw["gold"]["total"]
# item_data[item_name]["stats"] = item_data_raw["stats"]
# item_data[item_name]["effect"] = item_data_raw["effect"]

# return item_data





# # def get_champion_image_data():
# # return


# # def get_item_image_data(item_num):
# # "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/item/1001.png"
# # return