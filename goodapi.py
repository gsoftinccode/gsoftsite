import flask
from flask import request, jsonify

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# -------------------------------------------------------


@app.route('/process', methods=['POST','GET'])  
def process():
    try: 
        book = {"id":376236727, "name":"Computer Science Essentials","author":"Hari Prasaad","year":2003}

        return jsonify(book)
    except Exception as e:
        return "Image processing could not complete:\n"+ str(e)


@app.route('/home', methods=['POST','GET'])  
def process():
    try: 
        

        return jsonify({"greetongs": "Greetings every one over there"})
    except Exception as e:

        return "There was an error somewhere:\n"+ str(e)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')