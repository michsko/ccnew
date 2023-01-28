import json

def run():
	volebni_okrsky = json.load(open('scripts/volebni_okrsky-simple.json', 'r'))
	print(volebni_okrsky['features'][0])
	

