# IMPORT
import pickle
import consts
import requests


# common
def log(msg: str, type="err") -> None:
	"""Logs messages to the terminal

	Args:
		msg: any string
		type: type of the log
	"""
	if type == "err":
		print(f"ERROR: {msg}")
	elif type == "war":
		print(f"WARNING: {msg}")
	else:
		print(f"{type.upper()}: {msg}")


def deco(text: str, no_of_dashes=0, bottom=True, top=True) -> None:
	"""Prints dashes above and below a text

	Args:
		text: any string
		no_of_dashes: no of dashes to print (will use default value if set to 0)
		bottom: if True, prints dashes below the text
		top: if True, prints dashes above the text
	"""
	# setting dashes variable
	if no_of_dashes:
		dashes = "-"*no_of_dashes
	else:
		dashes = "-"*consts.no_of_dashes

	# decorating
	if top:
		print(dashes)
	if text:
		print(text)
	if bottom:
		print(dashes)


def capital(text: str) -> str:
	"""Capitalizes the first letter of a string

	Args:
		text: any string
	Returns:
		str: better text
	"""
	# capitalizing the first letter of a string
	return text[0].upper() + text[1:]


def user_input(text: str) -> input:
	"""Makes inputs a little bit nicer

	Args:
		text: any string
	Returns:
		input: user input
	"""
	# capitalizing user input
	return input(capital(text) + ": ")


# def read_bin(file_path: str) -> list:
# 	file = open(file_path, "rb")
# 	data = pickle.load(file)
# 	file.close()
# 	return data


def api_data(url: str) -> dict:
	"""Sends a get request to an API and parses the received data to json

	Args:
		url: url of the api
	Returns:
		dictionary: received data
	"""
	try:
		data = requests.get(url)
	except requests.HTTPError:
		log("Please check your internet connection!")
	else:
		return data.json()