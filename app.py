#py -m pip install --user virtualenv
#python -m venv env
#.\env\Scripts\activate
#pip install flask

from flask import Flask, make_response, json, jsonify
from mock import Seed

app = Flask(__name__)
#this prevent the response return in alphabetical order
app.config['JSON_SORT_KEYS'] = False

#_____________________________________________________________________________

@app.route("/v1/allseeds",methods=['GET'])
def a() :
    return make_response(
        jsonify(
            
              message='200',
              seed_data = Seed
                
        )
    )
    

#_____________________________________________________________________________

if __name__ == '__main__':

    print("server read to go")
    app.run(debug=True, port=8080)