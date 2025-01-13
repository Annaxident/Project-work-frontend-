from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "136aba0cd611a36e9fbcfe5a2c695a88d4e89c33be32a6a0de2f8c2c7beb914e"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///InfraTEL.db"

db = SQLAlchemy(app)

from flask import render_template,url_for,request,jsonify

@app.route("/")
@app.route("/home")
def home():
    return render_template("registrazione_edifici.html")

@app.route('/api/registrazione_edificio', methods=['POST',"GET"])
def registrazione_edificio():
    # Get the JSON data sent in the request
    data = request.get_json()  # The 'request.get_json()' method parses the incoming JSON
    
    if not data.get('indirizzo') or not data.get('codiceCatastale') or not data.get('tipoEdificio') or not data.get('dataPredisposizione'):
        return jsonify({'error': 'Tutti i campi sono obbligatori.'}), 400
    
    new_building = {
        'indirizzo': data['indirizzo'],
        'codiceCatastale': data['codiceCatastale'],
        'tipoEdificio': data['tipoEdificio'],
        'dataPredisposizione': data['dataPredisposizione']
    }

    print(new_building)
    return jsonify("Success")

@app.route("/api/confirm_request", methods = ["POST","GET"])
def confirm_request():
    print("It's working!!")
    return jsonify("Success")


if __name__ == "__main__":
    app.run(debug=True)

