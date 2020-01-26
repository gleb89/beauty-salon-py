import os, json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def reade_content_json(path_to_file:str):
    with open( os.path.join(BASE_DIR, path_to_file), encoding='utf-8' ) as file:
        return json.load(file)