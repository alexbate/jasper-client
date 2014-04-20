import re
import json
import urllib2

WORDS = ["LUNCH", "DINNER"]

def containsLunch(text):
	return bool(re.search(r'\b(lunch)\b', text, re.IGNORECASE))

def containsDinner(text):
	return bool(re.search(r'\b(dinner)\b', text, re.IGNORECASE))

def getTodaysMenus:
	asString = urllib2.urlopen('http://rsa33.user.srcf.net/gr_menu.php').read()
	return json.loads(asString)['menus'][0]

def readMenu(menu):
	for item in menu:
		mic.say(item['item'])

def handle(text, mic, profile):
	today = getTodaysMenus()
	if containsLunch(text) and containsDinner(text):
		mic.say("I'm not sure which meal you want to know about.")
	elif containsLunch(text):
		mic.say("Today's lunch menu is:")
		readMenu(today['lunch'])
	elif containsDinner(text):
		mic.say("Today's dinner menu is:")
		readMenu(today['dinner'])
	else:
		mic.say("I'm not sure which meal you want to know about.")


def isValid(text):
    """
        Returns True if the input is related to lunch or dinner.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(lunch|dinner)\b', text, re.IGNORECASE))