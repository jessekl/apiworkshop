import requests
import json
import os

def getImage(search_text):
	params = {
	    'method': 'flickr.photos.search',
	    'api_key': 'a9fafbae9fc10adf9c4d1e65b5181b57',
	    'text': str(search_text),
	    'safe_search': 1,
	    'content_type': 1,
	    'per_page': 1,
	    'format': 'json',
	    'nojsoncallback': 1,
	    'sort': 'relevance'
	}

	responses = requests.get('https://api.flickr.com/services/rest/', params=params).json()
	
	farm_id= str(responses["photos"]["photo"][0]["farm"])
	server_id = str(responses["photos"]["photo"][0]["server"])
	img_id = str(responses["photos"]["photo"][0]["id"])
	img_secret = str(responses["photos"]["photo"][0]["secret"])
	img_url = 'https://farm'+farm_id+'.staticflickr.com/'+server_id+'/'+img_id+'_'+img_secret+'.jpg'
	
	image = requests.get(img_url)

	fname = os.path.join(".", os.path.basename(image.url))
	f = open(fname,'wb')
	f.write(image.content)
	f.close()

	return fname

