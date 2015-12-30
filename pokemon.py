# A command line interface to deal with pokemons and get to know about them.
# Future plans: Turn complete CLI into GUI using Kivy.

#importing libraries.
import pykemon
import urllib
import urllib2
import json
import requests
# Menu function

def menu():
	menuContent = """Welcome to Pokeeper.
	Menu
	------------------------------------
	1. Search for a pokemon by Pokemon ID
	2. Search for a pokemon by name.
	------------------------------------
	"""
	return menuContent

#Function to return pokemon details by Pokemon ID

def searchPokemonByID(id):
	url = 'http://pokeapi.co/api/v1/pokemon/'+str(id)
	print url
	response = requests.get(url)
	retrievedData = response.json()
	#Printing all important data.

	print 'Pokemon Name : ' + retrievedData['name']
	print 'Pokedex ID : ' + str(retrievedData['pkdx_id'])
	print 'Species : ' + retrievedData['species']
	print 'Weight of Pokemon : ' + retrievedData['weight']
	print 'Height of Pokemon : ' + retrievedData['height']
	print 'Gets Evolved to :' + retrievedData['evolutions'][0]['to']
	print 'Abilities : '
	abilityCounter = 1
	for abilityName in retrievedData['abilities']:
		print str(abilityCounter) + '). ' +  abilityName['name']
		abilityCounter = abilityCounter+1 #Increase ability Index
	print 'Growth Rate : ' + str(retrievedData['growth_rate'])
	print 'How happy your Pokemon is : ' + str(retrievedData['happiness'])
	print 'Your Pokemon moves : '
	movesCounter = 1
	for movesOfThePokemon in retrievedData['moves']:
		print str(movesCounter) + '). ' +  movesOfThePokemon['name']
		movesCounter = movesCounter+1 #Increase ability Index
	
	
	




#Print menu on CLI...
print menu()

# Take user input for menu..

userInput = int(raw_input('Enter your choice here: '))

#Checking for the choice
#COMMENT -> I want to use dictionary here that will replace the switch case thing :P Just for fun

if userInput==1:
	pokemonID = int(raw_input('Please enter the Pokemon ID : (Eg. 1 for Bulbasaur, 25 for Pikachu ^_^ ) : '))
	searchPokemonByID(pokemonID)

