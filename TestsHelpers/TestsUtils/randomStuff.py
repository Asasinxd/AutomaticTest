import random
import string
import uuid
# import ulid

def randomWord(min, max = None, elements = string.ascii_letters):
	max = min if not max or max < min else max
	word = ""
	for i in range(random.randint(min, max)):
		word += random.choice(elements)

	return word

def randomUUID4():
	uuid4 = uuid.uuid4()
	return str(uuid4)

def randomULID():
	return "fndsjfndjskbfjk"
	# myulid = ulid.new()
	# return str(myulid)
	
def randomNumber(a, b):
	return random.randint(a, b)
