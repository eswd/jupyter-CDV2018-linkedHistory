import csv
import random
from flask import Flask
from flask_restful import Resource, Api


CSV_FILE = 'csv_new.csv'

app = Flask(__name__)
api = Api(app)


def random_data():
    """
    Return a random json daten snippet.
    """

    with open (CSV_FILE, 'r') as f:
            csv_data = csv.DictReader(f)
            rows = list(csv_data)
            random_row = random.randrange(0,len(rows))
            
            random_aktentitel = rows[random_row]['Aktentitel']

            return random_aktentitel



class HelloWorld(Resource):
    def get(self):



        return {'Titel': random_data()}

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
