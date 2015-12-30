# A command line interface to deal with pokemons and get to know about them.
# Future plans: Turn complete CLI into GUI using Kivy.

#importing libraries.
import pykemon
import urllib
import urllib2
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
	response = urllib.urlopen(url)
	pokeData = response.read()
	return pokeData
#Print menu on CLI...
print menu()

# Take user input for menu..

userInput = int(raw_input('Enter your choice here: '))

#Checking for the choice
#COMMENT -> I want to use dictionary here that will replace the switch case thing :P Just for fun

if userInput==1:
	pokemonID = int(raw_input('Please enter the Pokemon ID : (Eg. 1 for Bulbasaur, 25 for Pikachu ^_^ ) : '))
	print searchPokemonByID(pokemonID)

