import requests
import random

import urllib
from io import BytesIO
from PIL import Image

def get_random_pokemon(max = None):
	Pokemon = RandomPokemon(max)
	return Pokemon
	
def get_pokemon_count():
	url = 'https://pokeapi.co/api/v2/pokemon-species/'
	r = requests.get(url)
	species_json = r.json()
	pokemon_count = species_json['count']
	return pokemon_count
	
def get_pokemon_by_id(id):
	url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
	r = requests.get(url)
	pokemon = r.json()
	return pokemon

class RandomPokemon:
	def __init__(self,max):
		max_id = max if (max and max >= 4) else (get_pokemon_count())
		self.id =  random.randint(1,max_id)
		self.sprite = {'width':0, 'height':0}
		pokemon_json = get_pokemon_by_id(self.id)
		
		self.name = pokemon_json['species']['name'].capitalize()
		
		self.sprite['url'] = pokemon_json['sprites']['front_default']
		
		if(self.sprite['url']):
			file = BytesIO(urllib.request.urlopen(self.sprite['url']).read())
			im=Image.open(file)
			self.sprite['width'], self.sprite['height'] = im.size
		
		