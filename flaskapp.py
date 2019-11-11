from flask import Flask, request
from flask_restful import Resource, Api
import setlists

app = Flask(__name__)
api = Api(app)


class SongCheck(Resource):
   def get(self,song,date):
        result = setlists.song_was_played(song,date)
        return {'date:': date, 'song': song,'result':result}

api.add_resource(SongCheck, '/song/<song>/date/<date>')

if __name__ == '__main__':
    app.run(debug=True)