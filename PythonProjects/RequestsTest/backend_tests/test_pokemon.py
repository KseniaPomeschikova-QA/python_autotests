import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-type': 'application/json',  
          'trainer_token': '152171f74cf75df00ae10a5b5ed999d7'
}
ID_TRAINER = 3580

def test_get_trainers_code():
    """
    1. Get trainers; status code
    """
    response = requests.get(url=f'{URL}/trainers', timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_name():
    """
    2. Get trainers; trainer name
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': ID_TRAINER}, timeout=5)
    assert response.json()['trainer_name'] == 'Ксения', 'Unexpected trainer name'