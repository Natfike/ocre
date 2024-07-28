from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import json
import os

app = Flask(__name__)
CORS(app)
api = Api(app, version='0.1', title='Pipeline', description='Documentation for the pipeline',
          default="Pipeline", default_label="All endpoints for the pipeline", doc="/api/docs")

@api.route("/bossdata")
class Pipeline(Resource):
    @api.doc(description='get data')
    def get(self):
        chemin_fichier = 'ressources/json/boss.json'
        with open(chemin_fichier, 'r', encoding="UTF-8") as fichier:
            donnees = json.load(fichier)
        return donnees

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV')
    if env == 'production':
        app.run(host='0.0.0.0', port=5010)
    else:
        app.run(host='localhost', port=5000)