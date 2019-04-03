from django.shortcuts import render
from django.template import loader
from .models import *
from django.http import HttpResponse

from . import services

import sys
import os

import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def index(request, max_id = None):
	
	Pokemon = services.get_random_pokemon(max_id)
	id = str(Pokemon.id)
	
	Poke_Names = []
	Poke_Names.append(Pokemon.name)
	
	
	for i in range(3):
		Other_Pokemon = services.get_random_pokemon(max_id)
		while(Other_Pokemon.name in Poke_Names):
			Other_Pokemon = services.get_random_pokemon(max_id)
		Poke_Names.append(Other_Pokemon.name)
	
	random.shuffle(Poke_Names)
	
	context = {'pokemon':Pokemon, 'poke_names':Poke_Names}
	
	return render(request, 'whos_that/index.html', context)


		
	
