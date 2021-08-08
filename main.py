import requests
from pprint import pprint

def id_hero(name):
    response = requests.get(API_BASE_URL + '/search/' + name)
    full_information_hero = response.json()['results']
    for search_for_id in full_information_hero:
        if name == search_for_id['name']:
            id = search_for_id['id']
            return id

def search_intelligence_heroes(id):
    response = requests.get(API_BASE_URL + id)
    intelligence = response.json()['powerstats']['intelligence']
    return intelligence

def structure_intelligence_heroes(name):
    id = id_hero(name)
    intelligence_heroes.setdefault(name)
    intelligence_heroes[name] = int(search_intelligence_heroes(id))
    return intelligence_heroes

API_BASE_URL = ('https://superheroapi.com/api/2619421814940190/')
intelligence_heroes = {}
max_intelligence = 0

name = 'Hulk'
intelligence_heroes = structure_intelligence_heroes(name)

name = 'Captain America'
intelligence_heroes = structure_intelligence_heroes(name)

name = 'Thanos'
intelligence_heroes = structure_intelligence_heroes(name)

for hero, intelligence in intelligence_heroes.items():
    if intelligence > max_intelligence:
        superhero = hero
        max_intelligence = intelligence
pprint(f'Самый умный супергерой {superhero}, у него {intelligence} интеллекта')