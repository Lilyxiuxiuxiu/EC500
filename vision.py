#export GOOGLE_APPLICATION_CREDENTIALS="/Users/Lily/desktop/ec500/EC500HW1-90ccfccfbb71.json"

import io
import os
import json
import glob

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

dictionary = {}
for i in glob.glob('*.jpg'):
# The name of the image file to annotate
	file_name = os.path.join(
		os.path.dirname(__file__),
		i)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

	image_list = []
	response = client.label_detection(image=image)
	for labels in response.label_annotations:
		entry = ["mid: "+labels.mid, "description" + labels.description, "score: " + str(labels.score), "topicality: " + str(labels.topicality)]
		image_list.append(entry)

	dictionary[i] = image_list 

with open('labels.json', 'w')  as outfile:
	json.dump(dictionary, outfile, indent = 4, sort_keys=True)
