"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-type': 'application/json',  
          'trainer_token': '152171f74cf75df00ae10a5b5ed999d7'
}
BODY = {
    'name': 'Бульбазавр',
    'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
}

response = requests.post(url=f'{URL}/pokemons', json=BODY, headers=HEADER, timeout=5)
print(f'Создание покемона. Ответ в виде объекта json: {response.text}')

ID = response.json()["id"]

BODY2 = {
    "pokemon_id": ID,
    "name": "Другой Бульбазавр"
}

response2 = requests.patch(url=f'{URL}/pokemons', json=BODY2, headers=HEADER, timeout=5)
print(f'Изменение имени. Ответ в виде объекта json: {response2.text}')

BODY3 = {
    "pokemon_id": ID
}

response3 = requests.post(url=f'{URL}/trainers/add_pokeball', json=BODY3, headers=HEADER, timeout=5)
print(f'Покемон в покеболе. Ответ в виде объекта json: {response3.text}')