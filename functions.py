# MADE BY
#  ____   ___  __  __ ___ _     
# / ___| / _ \|  \/  |_ _| |    
# \___ \| | | | |\/| || || |    
#  ___) | |_| | |  | || || |___ 
# |____/ \___/|_|  |_|___|_____|
# 

# IMPORT
import pickle
import figlets

# FUNCTIONS
def get_max_length(text):
	# checking if text has newline character
	if "\n" in text:

		# creating a list of lines ["asdf", "asdfasdf"]
		text_list = text.splitlines()

		# creating a list of the lengths of the lines
		list_of_lengths = list(map(len, text_list))
		return max(list_of_lengths)
	else:
		return len(text)


def deco(text, no_of_dashes=0, bottom=True, top=True):
	# getting the length of the longest line
	max_length = get_max_length(text)

	# setting dashes variable
	if no_of_dashes:
		dashes = "-"*no_of_dashes
	else:
		dashes = "-"*max_length

	# decorating
	if top:
		print(dashes)

	if text:
		print(text)

	if bottom:
		print(dashes)

def capital(text):
	# capitalizing the first letter of a string
	return text[0].upper() + text[1:].lower()

def user_input(text):
	# capitalizing user input
	return input(capital(text) + ": ")

def read_bin(file_path):
	file = open(file_path, "rb")
	data = pickle.load(file)
	file.close()
	return data