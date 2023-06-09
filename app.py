#py -m pip install --user virtualenv
#python -m venv env
#.\env\Scripts\activate
#pip install flask

from flask import Flask, make_response, json, jsonify
from feedback import Feedbacks
from companies import CompaniesData

app = Flask(__name__)
#this prevent the response return in alphabetical order

app.config['JSON_SORT_KEYS'] = False


#_____________________________________________________________________________

@app.route("/v1/feedbacks",methods=['GET'])
def peoples_feedbacks() :
    return make_response(
        jsonify(
            
              message='200',
              data = Feedbacks
                
        )
    )
    
@app.route("/v1/companie",methods=['GET'])
def companies_friends():
    return make_response(
        jsonify(
            
            message = '200',
            data = CompaniesData
        )
    )


#_____________________________________________________________________________

if __name__ == '__main__':

    print("server read to go")
    app.run(debug=True, port=8080)

    #pip freeze > "requirements.txt"