'''
Calculates the amount of HP damage user outputs to static opponent

user_data:
{
"champion_name": STRING
"champion_level": INTEGER (1...18)
"items": LIST[STRING]
}

opponent_data: {
"champion_name": STRING
"champion_level": INTEGER (1...18)
"items": LIST[STRING]
}

abilities: LIST[INTEGER] ???

Returns a DICTIONARY value of calculated HP damage output
'''
def generate_damage_output(p1_data, p2_data, ability_seq):
# get champion + item data from CDN cache (for now just from JSON dir)

    # player 1 (user) - champion, champion level, and items
    p1_champ = p1_data["champion_name"]
    p1_level = p1_data["champion_level"]
    p1_items = p1_data["items"]

    # player 2 (opponent) - champion, champion level, and items
    p2_champ = p2_data["champion_name"]
    p2_level = p2_data["champion_level"]
    p2_items = p2_data["items"]

    # champion base stats for both players
    p1_base = get_champion_stats(p1_champ, p1_level)
    p2_base = get_champion_stats(p2_champ, p2_level)

    # item stat modifications for both players
    p1_item_mods = get_item_stats(p1_items)
    p2_item_mods = get_item_stats(p2_items)

    return calculate_total_damage(p1_champ, p2_champ, p1_base, p2_base, p1_item_mods, p2_item_mods, abilities)



def get_champion_stats(champion, level, champion_data):
    return



'''
hp_flat
hp_percent
mp_flat
mp_percent
ad_flat
ad_percent
ap_flat
ap_percent
armor_pen_flat
armor_pen_percent
magic_pen_flat
magic_pen_percent
armor_flat
armor_percent
magic_resist_flat
magic_resist_percent
'''
def get_item_stats(item_name, item_data):
    return


def calculate_auto_damage(p1_ad, p1_armor_pen, p2_armor):
    damage_reduction = armor/(100 + armor)
    return


def calculate_spell_damage(p1_ap, p1_magic_pen, p2_magic_resist, spell):
    damage_reduction = magic_resist/(100 + magic_resist)
    return


def calculate_total_damage(p1_champ, p2_champ, p1_base, p2_base, p1_item_mods, p2_item_mods, abilities):
    
    champion_dispatch = 
    { 
        'Aatrox': 
        'Ahri
        'Akali
        'Alistar
        'Amumu
        'Anivia
        'Annie
        'Aphelios
        'Ashe
        'AurelionSol
        'Azir
        'Bard
        'Blitzcrank
        'Brand
        'Braum
        'Caitlyn
        'Camille
        'Cassiopeia
        'Chogath
        'Corki
        'Darius
        'Diana
        'Draven
        'DrMundo
        'Ekko
        'Elise
        'Evelynn
        'Ezreal
        'Fiddlesticks
        'Fiora
        'Fizz
        'Galio
        'Gangplank
        'Garen
        'Gnar
        'Gragas
        'Graves
        'Hecarim
        'Heimerdinger
        'Illaoi
        'Irelia
        'Ivern
        'Janna
        'JarvanIV
        'Jax
        'Jayce
        'Jhin
        'Jinx
        'Kaisa
        'Kalista
        'Karma
        'Karthus
        'Kassadin
        'Katarina
        'Kayle
        'Kayn
        'Kennen
        'Khazix
        'Kindred
        'Kled
        'KogMaw
        'Leblanc
        'LeeSin
        'Leona
        'Lillia
        'Lissandra
        'Lucian
        'Lulu
        'Lux
        'Malphite
        'Malzahar
        'Maokai
        'MasterYi
        'MissFortune
        'MonkeyKing
        'Mordekaiser
        'Morgana
        'Nami
        'Nasus
        'Nautilus
        'Neeko
        'Nidalee
        'Nocturne
        'Nunu
        'Olaf
        'Orianna
        'Ornn
        'Pantheon
        'Poppy
        'Pyke
        'Qiyana
        'Quinn
        'Rakan
        'Rammus
        'RekSai
        'Renekton
        'Rengar
        'Riven
        'Rumble
        'Ryze
        'Samira
        'Sejuani
        'Senna
        'Seraphine
        'Sett
        'Shaco
        'Shen
        'Shyvana
        'Singed
        'Sion
        'Sivir
        'Skarner
        'Sona
        'Soraka
        'Swain
        'Sylas
        'Syndra
        'TahmKench
        'Taliyah
        'Talon
        'Taric
        'Teemo
        'Thresh
        'Tristana
        'Trundle
        'Tryndamere
        'TwistedFate
        'Twitch
        'Udyr
        'Urgot
        'Varus
        'Vayne
        'Veigar
        'Velkoz
        'Vi
        'Viktor
        'Vladimir
        'Volibear
        'Warwick
        'Xayah
        'Xerath
        'XinZhao
        'Yasuo
        'Yone
        'Yorick
        'Yuumi
        'Zac
        'Zed
        'Ziggs
        'Zilean
        'Zoe
        'Zyra
    }

    return champion_dispatch.get(p1_champ)

    def aatrox():
        return


    def ahri():
        return
