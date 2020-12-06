import collections
import ddragon_api
import json
import os
import requests
import shutil


CHAMPION_LOADING_IMAGE_EXT = "_0.jpg"
CHAMPION_SQUARE_IMAGE_EXT = ".png"

PATCH_PATH = "patch_versions"
DATA_PATH = "data"
IMAGE_PATH = "images"

CHAMPION_LOADING_PATH_EXT = "champion_loading"
CHAMPION_SQUARE_PATH_EXT = "champion_square"

def generate_patch_data():
    current_patch =  ddragon_api.get_current_patch()
    champion_list = ddragon_api.get_all_champions(current_patch)

    if not os.path.isdir(PATCH_PATH + '/' + current_patch):
        os.mkdir(PATCH_PATH + '/' + current_patch)

    if not os.path.isdir(PATCH_PATH + '/' + current_patch + '/' + IMAGE_PATH):
        os.mkdir(PATCH_PATH + '/' + current_patch + '/' + IMAGE_PATH)

    print(champion_list)

    # generate_champion_loading_images(champion_list, current_patch)
    # generate_champion_square_images(champion_list, current_patch)



# # parse all champion data
# def generate_champion_data(patch_ver):

#     champion_data_all = ... CHAMPION_URL + patch_version
#     champion_names = []
#     champion_data = collections.defaultdict()

#     for champion_name in champion_data:
#     champion_names.append(champion_name)

#     return champion_data



'''
Generates champion loading images for patch version
'''
def generate_champion_loading_images(champion_list, patch_version):

    file_path = PATCH_PATH + '/' + patch_version + '/' + IMAGE_PATH + '/' + CHAMPION_LOADING_PATH_EXT
    
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    for champion in champion_list:
        image_url = ddragon_api.BASE_URL + ddragon_api.CHAMPION_LOADING_IMAGE_EXT + champion + "_0.jpg"
        filename = file_path + '/' + champion + ".jpg"
        response = requests.get(image_url, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(response.raw, f)

    return "200"


'''
Generates champion square asset images for patch version
'''
def generate_champion_square_images(champion_list, patch_version):

    file_path = PATCH_PATH + '/' + patch_version + '/' + IMAGE_PATH + '/' + CHAMPION_SQUARE_PATH_EXT
    
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    for champion in champion_list:
        image_url = ddragon_api.BASE_URL + '/' + patch_version + ddragon_api.CHAMPION_SQUARE_IMAGE_EXT + champion + ".png"
        filename = file_path + '/' + champion + ".png"
        response = requests.get(image_url, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(response.raw, f)

    return "200"


'''
Generates item images for patch version
'''
def generate_item_images(item_list, patch_version):

    file_path = PATCH_PATH + '/' + patch_version + '/' + IMAGE_PATH + '/' + CHAMPION_SQUARE_PATH_EXT
    
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    for champion in champion_list:
        image_url = ddragon_api.BASE_URL + '/' + patch_version + ddragon_api.CHAMPION_SQUARE_IMAGE_EXT + champion + ".png"
        filename = file_path + '/' + champion + ".png"
        response = requests.get(image_url, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(response.raw, f)

    return "200"


'''
Generates champion ability images for patch version
'''
def generate_ability_images(item_list, patch_version):

    file_path = PATCH_PATH + '/' + patch_version + '/' + IMAGE_PATH + '/' + CHAMPION_SQUARE_PATH_EXT
    
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    for champion in champion_list:
        image_url = ddragon_api.BASE_URL + '/' + patch_version + ddragon_api.CHAMPION_SQUARE_IMAGE_EXT + champion + ".png"
        filename = file_path + '/' + champion + ".png"
        response = requests.get(image_url, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(response.raw, f)

    return "200"


def update_patch_directory(patch_version):
    return


# def save_patch_data(file_path, data):
#     return



if __name__ == "__main__":  
    generate_patch_data()