import json
from flicker import getImage
from flask import Flask,send_file,jsonify,request

app = Flask(__name__)

@app.route('/api/search/<search_text>',methods=['GET'])
def search(search_text):
	image = getImage(str(search_text))
	return send_file(image, mimetype='image/jpg')


@app.route('/api/post',methods=['POST'])
def test():
    data = json.loads(request.data)
    print data
    return jsonify({'result':data})

if __name__ == "__main__":
	app.run(debug=True)
	#app.run(debug=True,host='159.203.93.163',port=80)

