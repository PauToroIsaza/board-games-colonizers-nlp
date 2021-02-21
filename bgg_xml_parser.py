import csv
import requests
import xml.etree.ElementTree as ET

class boardgame:
	def __init___(self, bgg_id):
		return 0

def createURL(bgg_id):
	url_prefix = 'https://www.boardgamegeek.com/xmlapi/boardgame/'
	url_suffix = '?stats=1'
	url = url_prefix + bgg_id + url_suffix
	return url

def loadXML(url):
	resp = requests.get(url)
	root = ET.fromstring(resp.content)
	return root

def parseXML(root):
	# Iterate through all elements (tags)
	getYear(root)
	getTitle(root)
	getDesc(root)
	getSubdomains(root)
	getCategories(root)
	getFamilies(root)
	getRank(root)
	getExpansion(root)

def getYear(root):
	for child in root.iter('yearpublished'):
		print(child.text)

def getTitle(root):
	primary_name = False
	children = list((root.iter('name')))

	while (primary_name == False):
		child = children.pop(0)

		if 'primary' in child.attrib:
			if child.attrib['primary'] == 'true':
				primary_name = True
	print(child.text)

def getDesc(root):
	for child in root.iter('description'):
		print(child.text)
		# Need to remove HTML and convert special charcters like apostrophes.

def getSubdomains(root):
	for child in root.iter('boardgamesubdomain'):
		print(child.text)

def getCategories(root):
	for child in root.iter('boardgamecategory'):
		print(child.text)

def getFamilies(root):
	for child in root.iter('boardgamefamily'):
		getContinents(child.text)
		getCountries(child.text)
		getThemes(child.text)

def getContinents(text):
	if 'Continent' in text:
		print(text)

def getCountries(text):
	if 'Country' in text:
		print(text)

def getThemes(text):
	if 'Theme' in text:
		print(text)

def getRank(root):
	for child in root.iter('rank'):
		if child.attrib['name'] == 'boardgame':
			print(child.attrib['value'])

def getExpansion(root):
	expansion = False
	for child in root.iter('boardgameexpansion'):
		if 'inbound' in child.attrib:
			if child.attrib['inbound'] == 'true':
				expansion = True
				break
	print(expansion)

def main():
	test_id = '265141'

	test_url = createURL(test_id)
	print(test_url)
	print("")

	test_tree = loadXML(test_url)

	parseXML(test_tree)

if __name__ == "__main__":
	main()